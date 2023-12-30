from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard as kb
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from folium import plugins
import pyproj

#Inicialize o navegador   
driver = webdriver.Chrome()