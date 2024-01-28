# Yet Another Chat App

We need your assistance in developing a chat application for a new device called Com-link. Com-link connects to similar devices via a cutting-edge network where we can send digits from 0 to 9 instead of binary 0 and 1. We have devised a new model of encoding, as described below.

## Example 1:

Given the key:
“r”, “sw”, “x”, “c”, “nm”, “q”, “yt”, “z”, “ab”

If we want to send the message “bat,” then the encoding result will be “99090770”.

- Two 9’s represent the second character in the ninth string, which is “b”.
- 0 acts as a delimiter.
- One 9 represents “a” as the first character in the 9th string is “a,” followed by 0 as a delimiter.
- For “t,” we use two 7’s.

If we want to send the message “goat,” encoding is not possible as “g” is not available in the key. If we want to send “BAT,” the result will be “09900900770.” Adding an extra “0” at the start of the character’s encoding turns it into uppercase.

## Example 2:

Given the key:
“1abc”, “2def”, “3ghi”, “4jkl”, “5mno”, “6pqr”, “7stu”, “8vwx”, “ 90yz”

If we want to send the message “5 Roses,” then the encoding result will be “5090066660555507702220770.”

- One 5 represents the first character in the fifth string, which is “5”.
- 0 acts as a delimiter.
- One 9 represents the space as the first character in the ninth string is a space, followed by a delimiter.
- For “R,” we use 0 for capitalization, followed by four 6’s and then a 0 delimiter.
- Four 5’s represent ‘o’ and so on.

On the receiving end, we transfer the encoded result back to the actual string using the same key by reversing the process.

## Input and Output:

### Input:
- The input will be read from a file.
- The first line of the file will contain the key.
- The second line will describe the operation, where 1 is for encode and 2 is for decode.
- The third line will contain the string to encode or decode.

### Output:
- The output will be a single line of encoded or decoded results or “Error” if decoding or encoding is not possible.

### Constraints:
- The key will have a maximum of 9 strings.
- Encoding and decoding of a UTF-8 character set is expected.
- Length of each string in the key: 0 to 100.
- 0 will always be the delimiter.
- 0 at the start will indicate conversion to uppercase.
- Length of string to encode or decode: 0 to 1,000,000.

## Sample 1:

Input:
```
“r”, “sw”, “x”, “c”, “nm”, “q”, “yt”, “z”, “ab”
1
bat
```

Output:
```
99090770
```

## Sample 2:

Input:
```
“r”, “sw”, “x”, “c”, “nm”, “q”, “yt”, “z”, “ab”
2
099090770
```

Output:
```
Bat
```

## Sample 3:

Input:
```
“r”, “sw”, “x”, “g”, “nm”, “q”, “yt”, “z”, “ab”
1
Cat
```

Output:
```
Error
```