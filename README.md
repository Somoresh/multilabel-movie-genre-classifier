# multilabel-movie-genre-classifier

# Objective
The primary objective of this initiative was to develop a multi-label text classification model tailored to predict movie genres based on their descriptions. The scope of the project encompassed various phases, including data acquisition, preprocessing, model development, deployment, and seamless integration with application programming interfaces (APIs).
The keys of 
**deployment\genre_types_encoded.json**
  shows the book genres.

# Data Collection

Data has been sourced from the official IMDB website listing.

The process of scraping movie details, including titles, descriptions, and genres, has been executed utilizing the Selenium library. The corresponding code is available in the scraper/movie_details_scrapper.py directory.

The data collection endeavor remains ongoing, and all gathered information is being stored in the data/imdv_movies.csv file.

Update: The number of collected movies has now reached 25000, pending further processing and training.

# Data Processing

Through meticulous preprocessing detailed in notebooks/Multilabel_Texr_Classification.ipynb, duplicates and missing values were efficiently handled. To enhance model accuracy, two infrequent genres from 24 genres, namely Film and Noir, were judiciously dropped from the dataset. This strategic decision ensures optimal training outcomes, as training with rare genres could compromise model performance. The resulting refined dataset can be accessed in the designated data folder, reflecting our commitment to meticulous data management and model optimization.

# Model Deployment
 The compressed model is deployed to HuggingFace Spaces Gradio App. I utilized the Gradio App to deploy the model.
 HuggingFace Spaces [Here](https://huggingface.co/spaces/Somoresh/movie-genre-classifier)
 ![Screenshot_18](https://github.com/Somoresh/multilabel-movie-genre-classifier/assets/45269154/0233dd3e-0248-47f2-8b67-331874c9590c)
