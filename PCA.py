{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sometimes the data may have too many variables such that most of the variables are correlated\n",
    "\n",
    "#Model on the whole data => poor accuracy\n",
    "\n",
    "# Soln- PCA\n",
    "\n",
    "# Working principle of PCA - dimensionality reduction\n",
    "\n",
    "# PCA - method of extracting important variables with a motive to capture as much info as possible\n",
    "#     - extracts low dimensional set of variables from a high dimensional set\n",
    "\n",
    "# Here we are not going to predict y\n",
    "# The PCA unsupervised learning approach tries to learn the strength of relationship of varaiables\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analysing eating habit, excercise habit and body shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "d=pd.DataFrame(columns=['Calory','Breakfast','Lunch','Dinner','Excercise','Body Shape'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "d.loc[0]=[1200,1,0,0,2,'Skinny']\n",
    "d.loc[1]=[2800,1,1,1,1,'Fat']\n",
    "d.loc[2]=[3500,2,2,1,0,'Skinny']\n",
    "d.loc[3]=[1400,0,1,0,3,'Skinny']\n",
    "d.loc[4]=[1600,1,0,2,0,'Normal']\n",
    "d.loc[5]=[3200,1,2,1,1,'Fat']\n",
    "d.loc[6]=[1750,1,0,0,1,'Skinny']\n",
    "d.loc[7]=[1600,1,0,0,0,'Skinny']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Calory</th>\n",
       "      <th>Breakfast</th>\n",
       "      <th>Lunch</th>\n",
       "      <th>Dinner</th>\n",
       "      <th>Excercise</th>\n",
       "      <th>Body Shape</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1200</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Skinny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2800</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Fat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3500</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Skinny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1400</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Skinny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1600</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>3200</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Fat</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1750</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Skinny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1600</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Skinny</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Calory Breakfast Lunch Dinner Excercise Body Shape\n",
       "0   1200         1     0      0         2     Skinny\n",
       "1   2800         1     1      1         1        Fat\n",
       "2   3500         2     2      1         0     Skinny\n",
       "3   1400         0     1      0         3     Skinny\n",
       "4   1600         1     0      2         0     Normal\n",
       "5   3200         1     2      1         1        Fat\n",
       "6   1750         1     0      0         1     Skinny\n",
       "7   1600         1     0      0         0     Skinny"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
