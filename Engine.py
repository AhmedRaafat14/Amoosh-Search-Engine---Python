"""
	This is a basic script to make very simple search engine, which you can import it in your code and use any function
		you need from it.
		Hope It help 
"""



import requests

# read all link data in one var
cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>

""",
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>

<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>

</body>
</html>

""",
}
#requests.get(test_url).content

"""
    get_page(url)  ==> to read the content of a web page
"""
def get_page(page_link):
    if page_link in cache:
        return cache[page_link]
    return ""
# ====================================================================== #
"""
    get_next_target(page) ==> to get next link in the web page
"""
def get_next_target(page):
    # start_link = 'has the value of the position where
    #               the '<a href=' occurs'
    start_link = page.find('<a href=')
    if start_link < 0:
        return None, 0
    # start_quote = 'has the value of the position of
    #               first quote aftert start_link'
    start_quote = page.find('"', start_link)
    # end_quote = 'has the value of the position of
    #               second quote aftert start_quote'
    end_quote   = page.find('"', start_quote + 1)
    # url = 'has the value of the string between the
    #       start_quote and end quote === 'Link' '
    url         = page[start_quote + 1:end_quote]
    return url, end_quote
# ====================================================================== #
"""
    get_all_links(page) ==> to get all fetched links in web page and add them
                            to 'links' list
"""
def get_all_links(page):
    # links = is a list contain all fetched links
    links = []
    while True:
        url, end_pos = get_next_target(page)
        if url:
            links.append(url)
            page = page[end_pos:]
        else:
            break
    return links
# ====================================================================== #
"""
    union(first_subset, second_subset)  ==> using to union 2 subsets in one set
"""
def union(first_subset, second_subset):
    # loobing through seond subset to add its elements to first subset
    for element in second_subset:
        # just add this element if inly if not actually exist
        if element not in first_subset:
            first_subset.append(element)
# ====================================================================== #
"""
    add_page_to_index(index, url, content)  ==> to add all crawled pages and its
                                         content to index list
"""
def add_page_to_index(index, url, url_content):
    """
       # Split all page content depending on 'space' to get all its words
       #   as a keywords and store them in one list ==> words
       # Ex.      if url_content =  "I Love Python"
       #                   so when we split it, it will be like this
       #          words = ['I', 'Love', 'Python']
       # then store them as keywords for this url
    """
    words  = url_content.split()
    # loop through words list and add them to index
    for word in words:
        add_to_index(index, word, url)
# ====================================================================== #
"""
    add_to_index(index, keyword, url)  ==> this function fill index list by data
"""
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
# ====================================================================== #
"""
    look_up(index, keyword)  ==> its a so simple method to just
                          look up 'keyword' if it exist in
                          index list return its url list
"""
def look_up(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None
# ====================================================================== #
"""
    crawl_web(seed)  = is a method to go slowely through a given seed
                       page and crawl all links in it
"""
def crawl_web(seed):
    # toCrawl  =  list contain the kernal or seed page
    toCrawl = [seed]
    # crawled  =  list contain all crawled pages
    crawled = []
    # index    =  dictionary contain all pages and its keywords indexed in it
    index = {}
    # graph    =  dictonary to builde link graph used for ranking pages
    graph = {}
    # Loop on toCrawl list
    while toCrawl:
        # page =  pop the wanted crawled page from tocrawl list
        page = toCrawl.pop()
        # Check first if this page is not crawled yet
        if page not in crawled:
            # get page content in ==> content var
            content = get_page(page)
            # add this page to index list
            add_page_to_index(index, page, content)
            # union toCrawl list with all new not crawled links
            outlinks = get_all_links(content)
            # Construct the graph dictonary
            graph[page] = outlinks
            union(toCrawl, outlinks)
            # Now, add this crawled page to crawled list
            crawled.append(page)
    return index, graph
# ====================================================================== #
"""
    compute_ranks(graph) ==> is a function work on graph to rank all pages in it
"""
def compute_ranks(graph):
    # d = is damping factor
    d = 0.8
    # numLoops = is the number of loops we will get through them in dictionary
    numLoops = 10
    # ranks = is a dictionary used to store all pages ranks
    ranks = {}
    # nPages = number of pages in the graph
    nPages = len(graph)
    # loop throght graph and make all pages ranked by this equation
    #               1.0 / nPages
    for page in graph:
        ranks[page] = 1.0 / nPages
    # Loop through graph numLoops times
    for i in range(0, numLoops):
        # newranks dictionary to store the result of this equation
        #       ((1-d)/npages) + E[d*ranks[node] / number of outlinks ==>len(graph[node]) ]
        #           E refer to sumission
        newranks = {}
        # loop through the graph
        for page in graph:
            # define newRank var to store the result of
            #           (1-d) / nPages for each page
            newrank = (1 - d) / nPages
            # loop through each node in the graph
            for node in graph:
                # check if the page url is exist in this node list
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    # return the ranks dictionary
    return ranks
# ====================================================================== #
"""
    lucky_search(index, ranks, keyword) ==> work on index, ranks dictionaries
                                     and user keyword to find best result
"""
def lucky_search(index, ranks, keyword):
    # define a list to store in it url list for keyword from index
    keyword_urls = []
    # get the url list for this keyword from index dictionary if exist
    if keyword in index:
        keyword_urls = index[keyword]
    else:
        return None
    # define a list to store just urls from 'ranks' dictionary and also
    # exist in 'keyword_urls'
    #print(ranks)
    rank_keyword_urls = []
    for rank in ranks:
        if rank in keyword_urls:
            rank_keyword_urls.append([rank , ranks[rank]])
    # return best ranked link"""
    return max(rank_keyword_urls)[0]
# ====================================================================== #

# Test Case
index, graph = crawl_web(test_url)
ranks = compute_ranks(graph)

print lucky_search(index, ranks, 'know')
