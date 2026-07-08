import asyncio
from playwright.async_api import async_playwright

class GhostScraper:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    async def activate(self):
        print("--- 幽靈小龍蝦正在啟動數位軀殼 ---")
        # 修正啟動語法：使用 async with 方式
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.context = await self.browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080}
        )
        self.page = await self.context.new_page()
        print("--- 數位軀殼已生成，準備潛入 ---")

    async def infiltrate(self, url):
        print(f"正在前往目標網域: {url}")
        try:
            await self.page.goto(url, wait_until='networkidle', timeout=60000)
            await self.page.wait_for_selector('body')
            content = await self.page.content()
            return content
        except Exception as e:
            print(f"潛入失敗: {e}")
            return None

    async def retreat(self):
        print("--- 幽靈小龍蝦正在撤離戰場 ---")
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

async def run_test_mission():
    target_url = "https://tw.tradingview.com/chart/?symbol=OANDA%3AXAUUSD"
    ops = GhostScraper()
    await ops.activate()
    html_content = await ops.infiltrate(target_url)
    if html_content:
        print(f"成功抓取到內容，長度: {len(html_content)}")
    else:
        print("任務失敗：無法進入該網站。")
    await ops.retreat()

if __name__ == "__main__":
    asyncio.run(run_test_mission())
