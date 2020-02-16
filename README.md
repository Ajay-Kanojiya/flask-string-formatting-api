# flask-string-formatting-api
Create 2 rest API using flask(or any other Python Framework) that does the following things
# First API
# To split string at n intervals:-
    a. Method - GET
    b. Arguments
        i. String
        ii. number
    c. Response(json)
    d. Working
        i. The API code should split the given string(from request) from
        behind at n regular interval and return the output as a API
        response
  # Example
      1.
      ● Input string - abrakadabra
      ● Input number - 8
      ● Output Response - abr akadabra
      2.
      ● Input string = 10101011011
      ● Input no = 5
      ● Output Response = 1 01010 11011
# Second API
# To calculate the frequency of each unique string in a given list calculate
  the frequency of each unique string in a given list
    a. Method - GET
    b. Arguments
      i. String
    c. Response(json)
    d. Working
        i. write an optimised program to calculate the frequency of
        each unique string in a given list
  #  Example
        1.
        a. Input String = “kasol, kasol, manali, delhi, delhi, manali,
        kasol”
        b. Output Response(json) = {“kasol”: 3, “manali”: 2, “delhi”: 2}
        2.
        a. Input String = “1, a, c, b, c , 1”
        b. Output Response(json) = {“1”: 2, “a”: 1, “b”: 1, “c”: 2 }
