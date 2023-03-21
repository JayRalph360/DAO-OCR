# importing the required libraries

from flask import Flask, render_template, request, redirect, url_for
from joblib import load

pipeline = load("randomforest.h5")
