import wikipediaapi as wiki

class Wiki:
    connection = wiki.Wikipedia(user_agent="LabaBot@Telegram : (https://web.telegram.org/k/#@llababot)", language="pt")
    
    @staticmethod
    def get_page(page : str) -> str | None:
        page = Wiki.connection.page(page)

        if page.exists():
            return page
        
        return 
