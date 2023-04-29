import re
import requests


class BingSearch(object):
    def __init__(self) -> None:
        self.session = requests.Session()
        # # Regular expressions to extract title, brief, and link
        self.title_pattern = re.compile("<a.target=..blank..target..(.*?)</a>")
        self.brief_pattern = re.compile("K=.SERP(.*?)</p>")
        self.link_pattern = re.compile(
            "(?<=(a.target=._blank..target=._blank..href=.))(.*?)(?=(..h=))"
        )

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31"
        }
        self.proxies = {
            "http": None,
            "https": None,
        }
        self.chunk_count = 1

    def find(self, search_query):
        """
        Searches Bing for the given query and returns a list of dictionaries
        containing the title and content for each search result.

        Args:
            search_query (str): The search query.

        Returns:
            List[Dict[str, str]]: A list of dictionaries, where each dictionary
            contains a 'title' and 'content' field for a search result.
        """
        url = "https://cn.bing.com/search?q={}".format(search_query)
        res = self.session.get(
            url, headers=self.headers, proxies=self.proxies, timeout=2
        )
        r = res.text

        title = self.title_pattern.findall(r)
        brief = self.brief_pattern.findall(r)
        link = self.link_pattern.findall(r)

        # 数据清洗
        clear_brief = []
        for i in brief:
            tmp = re.sub("<[^<]+?>", "", i).replace("\n", "").strip()
            tmp1 = re.sub("^.*&ensp;", "", tmp).replace("\n", "").strip()
            tmp2 = re.sub("^.*>", "", tmp1).replace("\n", "").strip()
            clear_brief.append(tmp2)

        clear_title = []
        for i in title:
            tmp = re.sub("^.*?>", "", i).replace("\n", "").strip()
            tmp2 = re.sub("<[^<]+?>", "", tmp).replace("\n", "").strip()
            clear_title.append(tmp2)
        res = [
            {
                "title": "[" + clear_title[i] + "](" + link[i][1] + ")",
                "content": clear_brief[i],
            }
            for i in range(min(self.chunk_count, len(brief)))
        ]
        return res


if __name__ == "__main__":
    bing_search = BingSearch()
    print(bing_search.find("你好"))
