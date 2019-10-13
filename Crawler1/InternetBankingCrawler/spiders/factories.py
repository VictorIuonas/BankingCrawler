from InternetBankingCrawler.spiders.services import LoginRequestService


def build_login_request_service() -> LoginRequestService:
    return LoginRequestService()
