# Rania-Search-Engine---Python
This is a basic script to make very simple search engine, which you can import it in your code and use any function you need from it.

# Cache 
  is a varible which contain all page data.

# get_page(page_link)
  This is method take a url as its parameter and search for it in cach varible
  and return it if is exist or return empty string if not.

# get_next_target(page)
      This is method take page url as its parameter then looping through it and fetch the next url in it.
      
      start_link
          Has the value of the position where the '<a href=' occurs
      start_quote
          Has the value of the position of first quote aftert start_link
      end_quote
          Has the value of the position of second quote aftert start_quote
      url
          Has the value of the string between the start_quote and end quote ===> 'Link'

# get_all_links(page)
      To get all fetched links in web page and add them to 'links' list
      
      links
          Is a list contain all fetched links
          
# union(first_subset, second_subset)
      Using to union 2 subsets in one big set
      
# add_page_to_index(index, url, content)
      To add all crawled pages and its content to index list
      Split all page content depending on 'space' to get all its words
          as a keywords and store them in one list ==> words
      Ex.      if url_content =  "I Love Python"
                          so when we split it, it will be like this
                 words = ['I', 'Love', 'Python']
       then store them as keywords for this url

# add_to_index(index, keyword, url)
      This function fill index list by data.
      
# look_up(index, keyword)
      Its a so simple method to just look up 'keyword' if it exist in index list return its url list if not
      return 'None'

# crawl_web(seed)
      Its method take a seed link as parameter and then fetch all links in it and add them to crawled list
      and index dictionary, and then get first link it fetched it from seed page and crawl it and so on until
      index and graph dictionaries filled up and found a page without links in it
      
      toCrawl
          List contain the seed page and other pages which ready to be crawled
      crawled
          List contain all crawled pages
      index
          Dictionary contain all pages and its keywords indexed in it
      graph
          Dictonary to builde link graph used for ranking pages

# compute_ranks(graph)
      Its a method take graph as its parameter and then get all links in it and calculate its rank value
      using this equation :
              ((1-d)/npages) + E[d*ranks[node] / number of outlinks ==>len(graph[node]) ]
      d
          Is damping factor
      numLoops
          The number of loops we will get through them in dictionary {You can change it}
      nPages
          Number of pages in the graph
      ranks
          Dictionary used to store all pages with its ranking
          
# lucky_search(index, ranks, keyword)
       Work on index, ranks dictionaries and user keyword to find the best search result {return url}
       
       keyword_urls
            List to store in it url list for given keyword from index
        rank_keyword_urls
            List to store just urls from 'ranks' dictionary and also exist in 'keyword_urls'
            { store link and its rank }
            
# How you can test it ?
      Download the source code and first intalize the cache variable with the any page data you want
      then call the methods:
                        index, graph = crawl_web(test_url)
                        ranks = compute_ranks(graph)
                        print lucky_search(index, ranks, 'know')
      
      'know' is a keywoord used to test it depending on my intalize for cache vaible in source code
      and you can put this 3 lines at the end of file.
      
Have A Fun
