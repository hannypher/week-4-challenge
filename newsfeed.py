import click
import requests

# the apikey obtained from newsapi.org
API_KEY = 'f8c6919b09f245d59c4f5e2f6a134511'

@click.group()
def main():
        """
        NEWS FEED-version 1 ia a new app that gives you a list of four sources from which you chose one, 
        Then from your choice it returns a list of the top 10 headlines,
        The news headline has a title, description and a url in case the user needs to follow up
        The user also needs to have a valid news api created from http://www.newsapi.org
        """
        pass

@main.command()

def listsources():
        """ lists four sources from the API """
        main_url = "https://newsapi.org/v2/sources?apikey=f8c6919b09f245d59c4f5e2f6a134511"

        # fetching data in json format
        open_source = requests.get(main_url).json()

        # getting all articles in a string sources
        source = open_source["sources"]

        # empty list which will 
        # contain all trending newssources
        results = []

        for s in source:
                results.append(s["id"])


        for i in results[0:4]:
            print(i)


@main.command()
def topheadlines():
        """please enter your choice from the listsources"""
        newsSource = click.prompt("please enter your choice from listsources")

        main_url = "https://newsapi.org/v2/top-headlines?apikey=f8c6919b09f245d59c4f5e2f6a134511&sources="+newsSource

        # fetching data in json format
        open_topheadlines = requests.get(main_url).json()

        # getting all topheadlines in a string articles
        topheadlines = open_topheadlines["articles"]

        # empty list which will 
        # contain all trending newssources
        output = []

        for h in topheadlines:
            click.echo('\n')
            click.secho(click.style('TITLE: ' + h['title'], fg='red'))
            click.secho(click.wrap_text(h['description']))
            click.secho(click.style('DOMAIN: '+ h['url'], fg='blue'))


        for i in output[:11]:
            print(i)


if __name__ == '__main__':
        main()
