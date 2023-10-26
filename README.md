# Pushdown Automata (PDA)

Members:  
&emsp;Santiago Cardoso  
&emsp;Lucas Gabriel

Final work of the Linguagens Formais e Autômatos ​​(LFA) discipline, done in the Python programming language.

```
$ git clone https://github.com/santiagocardoso/simulador_automatos_com_pilha.git
```

Create a JSON file with the following example:
```json
{
   "type":"PDA",
   "pda":{
      "states":{
         "s0":[
            {
               "label":"a,,a",
               "next":"s0"
            },
            {
               "label":"b,,b",
               "next":"s0"
            },
            {
               "label":",,",
               "next":"s1"
            }
         ],
         "s1":[
            {
               "label":"a,a,",
               "next":"s1"
            },
            {
               "label":"b,b,",
               "next":"s1"
            }
         ]
      }
   },
   "start":"s0",
   "final":"s1",
   "tests":{
         "accept":"abba"
   }
}
```

Execution:  
&emsp;python3 pda.py
