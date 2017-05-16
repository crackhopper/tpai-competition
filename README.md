# tpai-competition
- clone the repo
- download the data from http://spabigdata-1253211098.file.myqcloud.com/pre.zip
- extract the files into `_data` directory
- run `python convert_data.py`

# feature extract
- run `python extract_features.py`

# model select
- run `python select_models.py`

# generate result
- run `python save_result.py`

# about notebook
- It is boilerplates for user to design their own experiment environment. Clone
  new notebooks based on them and do experiments on those new notebooks.
- The three notebook files are for developing custom data loader, feature
  extractor and estimator respectively.
- Please make sure not to update the boilerplate notebook.

# about config.py
- modify it as u like.
- do not push a custom one into the repo.

# about the project
- for initialize, you only need to run `python convert_data.py`
- for any update, you need
  - modify the config file as you like
  - run 
    - `python extract_features.py`
    - `python select_models.py`
    - `python save_resullt.py`

If you want to use it in another competition, just rewrite these four script,
then you'd be possible to get a working environment for further exploration.
Then you need to write different extractors and models in
`competition/featExtract` folder and `competition/models` folder.

