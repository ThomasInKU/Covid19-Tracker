# Covid19-Tracker
[![Build Status](https://travis-ci.com/lisbono2001/Covid19-Tracker.svg?branch=master)](https://travis-ci.com/lisbono2001/Covid19-Tracker) 
[![codecov](https://codecov.io/gh/lisbono2001/Covid19-Tracker/branch/master/graph/badge.svg)](https://codecov.io/gh/lisbono2001/Covid19-Tracker)
<a href="https://github.com/lisbono2001/Covid19-Tracker/issues">
   <img alt="Issues" src="https://img.shields.io/github/issues/lisbono2001/Covid19-Tracker?color=0088ff" />
</a>
<a href="https://github.com/lisbono2001/github-readme-stats/pulls">
   <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/lisbono2001/Covid19-Tracker?color=0088ff" />
</a>
## URL of the web application
[See our URL of the web application](https://covidtracker-isp.herokuapp.com/)    

## Description
This is a web-application that can show every Covid-19 case in Thailand 🇹🇭.  
Users can add Line bot that can be interacted with and send the information to users  (including cases and important information).  
Most benefit of this application is users can get information about Covid-19 through Line bot and on web-page.

### Installation
First you need to install virtualenv and pip
* #### Windows

```bash
python -m pip install --upgrade pip
python -m pip install virtualenv
```
* #### Linux/Macos
```bash
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
```

### Getting Start
1.Clone Covid19-Tracker repository to your local machine and navigate to the project directory
```shell
git clone https://github.com/lisbono2001/Covid19-Tracker.git
cd Covid19-Tracker/
```
2.Create virtual environment and activate it.
* #### Windows
```bash
virtualenv env
env\Scripts\activate
```
* #### Linux/Macos
```bash
virtualenv venv
source venv/bin/activate
```
3.Install all required software included in requirements.txt
```bash
pip install -r requirements.txt
```
4.Migrations
* #### Windows
```bash
python manage.py migrate
```
* #### Linux/Macos
```bash
python3 manage.py migrate
```
5.Run the server
* #### Windows
```bash
python manage.py runserver
```
* #### Linux/Macos
```bash
python3 manage.py runserver
```
## Contributing
Every pull requests are welcome. Please open an issue first to discuss what you would like to change.  [Read the contribution](contributing.md)

## Project Iterations  

### Iterations Plans
* [Iteration 1 Plan](https://github.com/lisbono2001/Covid19-Tracker/wiki/Iteration-1-plan)
* [Iteration 2 Plan](https://github.com/lisbono2001/Covid19-Tracker/wiki/Iteration-2-plan)
* [Iteration 3 Plan](https://github.com/lisbono2001/Covid19-Tracker/wiki/Iteration-3-plan)
* [Iteration 4 Plan](https://github.com/lisbono2001/Covid19-Tracker/wiki/Iteration-4-plan)
* [Iteration 5 Plan](https://github.com/lisbono2001/Covid19-Tracker/wiki/Iteration-5-plan)
* [Iteration 6 Plan](https://github.com/lisbono2001/Covid19-Tracker/wiki/Iteration-6-plan)
* [Iteration 7 Plan](https://github.com/lisbono2001/Covid19-Tracker/wiki/Iteration-7-plan)

### Project TaskBoards    
* [Iteration 1 TaskBoards](https://github.com/lisbono2001/Covid19-Tracker/projects/1)    
* [Iteration 2 TaskBoards](https://github.com/lisbono2001/Covid19-Tracker/projects/2)
* [Iteration 3 TaskBoards](https://github.com/lisbono2001/Covid19-Tracker/projects/3)
* [Iteration 4 TaskBoards](https://github.com/lisbono2001/Covid19-Tracker/projects/4)
* [Iteration 5 TaskBoards](https://github.com/lisbono2001/Covid19-Tracker/projects/5)
* [Iteration 6 TaskBoards](https://github.com/lisbono2001/Covid19-Tracker/projects/6)
* [Iteration 7 TaskBoards](https://github.com/lisbono2001/Covid19-Tracker/projects/7)

## Project Documents
* [Project Presentation Slide](https://docs.google.com/presentation/d/12TrLN7DaFByj_W0nC0guYkGCF7eRGC-enF77FvVeLyc/edit?usp=sharing)
* [Google Slide of the Iteration2(Demo1)](https://docs.google.com/presentation/d/14qMV3SfXerS6ZqlIU6QqADaq-o9OB24neuZzF2Wg8W4/edit?usp=sharing)
* [Google Slide of the Iteration3(Demo2)](https://docs.google.com/presentation/d/1644cAhMw_56MGKahJRFheus9vtq5G2nMFGxjAxFY4lk/edit?usp=sharing)
* [Google Slide of the Iteration4(Demo3)](https://docs.google.com/presentation/d/1q7hvfviI6Zbfiea9Jx7KZqt6942ZJalaiTW8-VWJNZc/edit?usp=sharing)
* [Google Doc of CovidTracker Bot](https://docs.google.com/document/d/1yZ44ohLjBxY3xdxLnVfxUchmPmGIvRqF8OUgX0xgOpg/edit?usp=sharing)
* [Code Review Checklist](https://github.com/lisbono2001/Covid19-Tracker/wiki/Code-Review-Checklist)
* [Code Review Procedure](https://github.com/lisbono2001/Covid19-Tracker/wiki/Code-Review-Procedure)  
  For deeper detail, be sure to check out [the wiki documentation](https://github.com/lisbono2001/Covid19-Tracker/wiki).

### License
[GNU](LICENSE.md)  
