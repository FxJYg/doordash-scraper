import asyncio
import os
from scrapybara import Scrapybara
from dotenv import load_dotenv
from undetected_playwright.async_api import async_playwright
import json

load_dotenv()

async def get_scrapybara_browser() -> str:
    """ Creates a browser instance on a Scrapybara machine """
    client = Scrapybara(api_key=os.getenv("SCRAPYBARA_API_KEY"))
    instance = client.start_browser()
    return instance

async def retrieve_menu_items(instance, start_url: str) -> list[dict]:
    """
    :args:
    instance: the scrapybara instance to use
    url: the initial url to navigate to

    :desc:
    this function navigates to {url}. then, it will collect the detailed
    data for each menu item in the store and return it.

    (hint: click a menu item, open dev tools -> network tab -> filter for
            "https://www.doordash.com/graphql/itemPage?operation=itemPage")

    one way to do this is to scroll through the page and click on each menu
    item.
 
    determine the most efficient way to collect this data.

    :returns:
    a list of menu items on the page, represented as dictionaries
    """
    print(instance.get_stream_url().stream_url)
    cdp_url = instance.get_cdp_url().cdp_url
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(cdp_url)
        context = await browser.new_context(viewport={"width": 1000, "height": 600})
        page = await context.new_page()

        await page.goto(start_url)

        menu_items = []
        #faster checking using name
        clicked_items = set()  # Track clicked items to avoid duplicates

        # Function to intercept GraphQL requests
        async def intercept_request(response):
            if "graphql/itemPage?operation=itemPage" in response.url:
                data = await response.json()
                if data['data']["itemPage"]["itemHeader"]["name"] not in clicked_items:
                    menu_items.append({data['data']["itemPage"]["itemHeader"]["name"] : data})
                    clicked_items.add(data['data']["itemPage"]["itemHeader"]["name"])

        # Attach request interception
        page.on("response", intercept_request)

        enter_address = page.locator('input[data-testid="AddressAutocompleteField"]')
        await enter_address.type("1", delay=100)
        await enter_address.press("Enter")
        
        close =page.locator("span").get_by_text("See Menu")
        await close.click()

        is_at_bottom = False
        while not is_at_bottom:
            #check if's the bottom of the page
            is_at_bottom = await page.evaluate("() => {return (window.innerHeight + window.scrollY) >= document.body.scrollHeight;}")

            #select all visible menu items
            menu_elements = await page.locator('div[data-anchor-id="MenuItem"]').all()

            #go back to original scroll location to ensure the items are still visible
            original_scroll_y = await page.evaluate("window.scrollY")

            #loop through each item to click
            for item in menu_elements:
                await item.click()
                close_button = page.locator('button[aria-label="Close"]')
                await close_button.click()
                await page.evaluate(f"window.scrollTo(0, {original_scroll_y});")


            # Scroll down
            await page.evaluate("window.scrollBy(0, 800);")
            
            # Allow new items to load
            await page.wait_for_timeout(1000) 
    
    return menu_items



async def main():
    instance = await get_scrapybara_browser()

    try:
        menu_list = await retrieve_menu_items(
            instance,
            "https://www.doordash.com/store/panda-express-san-francisco-980938/12722988/?event_type=autocomplete&pickup=false",
        )
    finally:
        # Be sure to close the browser instance after you're done!
        instance.stop()


if __name__ == "__main__":
    asyncio.run(main())
