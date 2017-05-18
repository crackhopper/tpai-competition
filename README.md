# tpai-competition
This is a tool box for data mining competitions.

# Run Toolbox
## Prepare 
- clone the repo
- download the data from http://spabigdata-1253211098.file.myqcloud.com/pre.zip
- extract the files into `_data` directory

## 0. convert data
- run `python run_0_convert_data.py`

## 1. extract feature
- run `python run_1_extract_features.py`

## 2. select model
- run `python run_2_select_models.py`

## 3. generate result
- run `python run_3_predict.py`

# Advance

## The boilerplates folder
They are notebook files used as boilerplates for user to design their own
experiment environment. Clone new notebooks based on them and do experiments on
those new notebooks.

## Configuration
- The default configuration file is `config.py`. You should not change that
  file.
- Make a new config file named `configCustom.py`. And replace the the defaullt
  config settings there.

## Basic steps to use this repo for other competitions:
1. clone the repo, and copy the boilerplates.
2. Design a data converter by experiment on the boilerplate
   - load datafiles into pandas.HDFStore. 
   - change the column name of label to be 'label'
   - save the training and test dataset by keys 'train' and 'test', respectively
   - merge some tables (that not used in train and test set directly)
   - run `python run_0_convert_data.py`, and it would generate a `store.db` file
     inside the `_data` directory
   
3. Design a feature extractor by experiment on the boilerplate
   - derive a class from `competition.extractors.BaseExtractor`.
   - experiment it.
   - save the code into folder `competition/extractors` and provide the
     `extractor` and `extractor_name` object.
   - modify `configCustom.py` to use this extractor.
   - run `python run_1_extract_features.py`, and it would generate a `*.db` file
     inside the `_extract` directory which stores the extracted training and
     test set.
   
4. Select a model by experiment on the boilerplate
   - derive a class from `competition.models.BaseModel`.
   - experiment it.
   - save the code into folder `competition/models` and provide the `estimator`
     and `estimator_name` object.
   - modify `configCustom.py` to use this estimator, and provide variable
     `tuned_parameters` as well as `para_name`.
   - run `python run_2_select_models.py`

5. Predict the test set.
   - run `python run_3_predict.py`

