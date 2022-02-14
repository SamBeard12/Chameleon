# Chameleon

Questions/ambiguities/assumptions for discussion:



1) What should ConstrainedInsert do/return if initial contains repeated values in different positions - e.g.:

    

    initial = ['cat', 'dog', 'monkey', 'lion', 'fish', 'aardvark', 'cat']

    before = ['dog']

    after = ['cat']



2) It is assumed that before==[] and/or after==[] are valid values and that item can therefore be inserted 

   at any position in initial. 



3) It is assumed that identifying all parameter errors is more important than outright performance.
