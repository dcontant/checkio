# checkio
solution to checkio mission: amsco-cipher

info agout this particular cipher as given by the mission's autor: bryukh 

 Let's look at the AMSCO cipher. This is a positional cipher with exchanges. You can easily encode or decode a message with 
 a pen and paper, that is of course, if you know the key.

The key is represented as a number that consist of unique digits from 1 to N. N is a length of the key. To encode message 
we should write a message in a matrix with N columns. The matrix is written row by row. In this process, one or two characters 
are alternately recorded in a field. One or two characters alternate in rows and in columns too (like a chessboard). The first 
element is single letter field (this is the arrangement for this mission). The last field can have single characters 
if there are not enough. Columns are then numbered with digits from the key in order. For example: using the key 312, 
the first column will be 3, the second is 1 and the third is 2. Lastly, you will write all characters in the columns as 
they were numbered in the most recent step. All white spaces and punctuation symbols are excluded while letters are in 
lowercase.

Let's look at this with an example. The message "Lorem ipsum dolor sit amet". And the key is 4123. The cut message 
is "loremipsumdolorsitamet". In matrix form it will be:

   4   1   2   3
   l  or   e  mi
  ps   u  md   o
   l  or   s  it
  am   e   t

Now write the columns as they are numbered in the ascending order - "oruore", "emdst", "mioit", "lpslam". 
The encoded message is "oruoreemdstmioitlpslam".

