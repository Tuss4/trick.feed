'''
Let's build a command line
search utility for trickfeed.
'''
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trickfeed.settings")

from trickfeed.models import Video


# The main function yo.
def main():
    query = raw_input('Enter your query: ')
    results = Video.objects.filter(title__icontains=query, is_tricking=True)
    if results:
    	print {x.title: x.youtube_url() for x in results}
    else:
    	print "No results found."
    print "Coolio."

if __name__ == '__main__':
    main()
