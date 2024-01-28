# Arbisoft Balloon Decoration Challenge

Arbisoft is excited to open its new office in Germany and wants to decorate it in a fun and colorful way. The office will be adorned with a repeating pattern of colorful balloons to create a lively atmosphere. These balloons come in three colors: orange (O), blue (B), and white (W). 

## Problem Statement

Decorating the large office space requires careful planning. Arbisoft has divided the office into sections, with different teams responsible for each section. Each team has a starting point and an ending point within the office. The challenge is to distribute the correct number of balloons to each team based on their assigned area and the balloon pattern.

To tackle this problem, Arbisoft seeks the expertise of coding wizards like you. You will be provided with a pattern of balloons represented as a string, along with starting and ending index parameters specifying each team's area. Your task is to write a code that determines the number of balloons of each color needed for decoration within a specific range.

## Input and Output

### Input:
- The input will be read from a file.
- The first line of the file will contain the balloon pattern.
- The second and third lines will specify the starting and ending indexes respectively.

### Output:
- The output will be a lowercase string indicating the number of blue, orange, and white balloons needed, in that order, along with their counts (e.g., "b12o5w7").

### Constraints:
- The starting and ending indexes may either be equal to or fall within the range of 0 to 100,000,000.
- Ending index > starting index 
- The length of the balloon pattern will be between 5 and 15 characters inclusive.

## Examples

### Sample 1:
```
Input:
bowbo
7
12

Output:
b2o2w2
```

### Sample 2:
```
Input:
owbowbob
17
48

Output:
b12o12w8
```

### Sample 3:
```
Input:
obbo
0
6478

Output:
b3240o3239w0
```

Let's make Arbisoft's new office a vibrant and enchanting space together! Happy coding!
