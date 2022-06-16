from icrawler.builtin import GoogleImageCrawler


class Crawler:
    """Crawler class used to get images:

    -query = string
    -start = (year, month, date)
    -end = (year, month, date)

    """

    def __init__(self, query: str, start: tuple, end: tuple, limit: int = 50):
        self.query = query
        self.start = start
        self.end = end
        self.limit = limit

    def get_images_google_images(self) -> bool:
        try:
            google_crawler = GoogleImageCrawler(
                feeder_threads=1,
                parser_threads=2,
                downloader_threads=4,
                storage={"root_dir": "./images"},
            )

            filters = dict(
                size="large",
                color="green",
                date=((self.start), (self.end)),  # pastweek
            )
            google_crawler.crawl(
                keyword=self.query,
                filters=filters,
                max_num=self.limit,
                file_idx_offset=0,
            )
            return True
        except Exception as e:
            print(e)
            return False
