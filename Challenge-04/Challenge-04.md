## ICC Champion Trophy 2025

You are an expert "Python Programmer." Below are the instructions provided in triple parenthesis. Your task is to solve the problem and create a Python script as the output.

### Problem Description

Pakistan is hosting the ICC Champion Trophy 2025, where the top eight ICC ranked teams will participate in fifteen matches across different venues in the country. With millions of people following the event online, the Pakistan Cricket Board aims to enhance fan engagement by predicting each team's win probability against all other participating teams a week in advance of the tournament.

The board has historical scorecards for all matches played among the participating teams, accessible via an (https://l0l6pp2i0k.execute-api.eu-north-1.amazonaws.com/default/icc_matches). The API returns a list of matches, each containing the scorecards of both teams. Here's the structure of the response:

```python
[
  {
    "date": "02/02/2022",
    "team1": "Pakistan",
    "team2": "India",
    "venue": "MCG",
    "scoreCardTeam1": [
      {
        "name": "Fakhar Zaman",
        "score": 53
      },
      ...
    ],
    "scoreCardTeam2": [
      {
        "name": "Virat",
        "score": 10
      },
      ...
    ]
  },
  ...
]
```

You've been hired to build the first version of this predictor. Your task is to write a program that takes two countries, A & B, as input and predicts the winning chances of each country out of a hundred based on the following criteria:

- Percentage of times Team A has scored more than Team B represents the winning chances of A, rounded to two decimal places.
- Percentage of times Team B has scored more than Team A represents the winning chances of B, rounded to two decimal places.
- Matches played in the current year have a weightage of 10. Weightage reduces by 1 with every year in the past. Matches played before 10 or more years have a weightage of 0.5.

#### Example:

Let’s say Pakistan and Australia have played 10 matches in history, five in 2024 and five in 2022. Pakistan scored more than Australia in two matches in 2024 and three matches in 2022. The weighted percentage of the number of times Pakistan won represents Pakistan's winning chances, which is 48.89% in this example. Similarly, the weighted percentage of the number of times Australia won represents Australia's winning chances.

### Input and Output

#### Input:
The input is read from a file containing names of two teams separated by a comma for which predictions are required.

#### Output:
The output will be the win prediction for the given teams in the same order, separated by a comma.

#### Notes:
- Current year is 2024.
- Each team has played a minimum of 10 matches with every other team.
- Team’s score is equivalent to the sum of each player’s score available in the scorecard.
- Skip the draws (matches where scores of both teams were equal).
- Country spellings in the input match exactly with those in the API response.

### Sample Input and Output

#### Sample 1
Input:
```
NewZealand,Pakistan
```
Output:
```
34.72%,65.28%
```

#### Sample 2
Input:
```
SriLanka,Netherlands
```
Output:
```
54.95%,45.05%
```

#### Sample 3
Input:
```
Pakistan,Netherlands
```
Output:
```
50.61%,49.39%
```

#### Input File Reading Instructions:
The input is read from a file, and the filename/path of the file is passed to your program as the first command-line argument. There is no fixed name for the input file. Do not hardcode the input file name.
