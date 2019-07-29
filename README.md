<h3>This is a K-means Cluster implementation in Python, with Pandas, Sklearn (K-means algorithm, preprocessing and metrics), and Matplotlib.</h3>

For search the perfect number of clusters, the Elbow method was used. Read more <a href="https://www.datanovia.com/en/lessons/determining-the-optimal-number-of-clusters-3-must-know-methods/">here</a>.

For avaliating the result, I'm used the Calinski and Harabaz Score. You find <a href="https://www.mathworks.com/help/stats/clustering.evaluation.calinskiharabaszevaluation-class.html">here</a>.

So, this is a experimental implementation. You can use on your search, but, exist <strong>best implementations</strong> around internet.

But you need learn now, let's go.

First, <a href="https://www.python.org/downloads/">install Python</a>.

Second, <a href="https://pandas.pydata.org/">install Pandas</a>, <a href="https://scikit-learn.org/">install Sklearn</a>, and <a href="https://matplotlib.org/">install Matplotlib</a>.

Now, create a folder and drop the monthour.csv. This data is a relacional list of hour and month Boston crimes. This data is discretized. Here the original dataset <a href="https://www.kaggle.com/ankkur13/boston-crime-data">data</a>. The objective is find relations of group used the month and hour atributtes. 

Third, find the perfect K with Elbow method. 

Fourth, <strong>read</strong> the file. The parameter 'error_bad_lines=False' is important because are hundreds and hundreds lines of data, so there may be badly formatted or corrupted data that is difficult to find.

Fifth, preprocessing. You can learn why <a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html">here</a>.

Now, we can instantiate the K-means. We have the number of clusters and that is everything. Why we used the K-means++ method? You can learn <a href="https://stats.stackexchange.com/questions/130888/k-means-vs-k-means">here</a>.

Sixth, go plot the graphs and centroids. What is a centroid? Centroid is like a grouping point or gravity point. There are you clusters.

Seventh, we need know how much we go it right. Calinski and Harabaz Score can help we.

tt: @lucasfeed










