
# coding: utf-8

# # CS 196 Spring 2017 Homework 3

# # Table of Contents
# ---
# 1. [Count Cycles](#Count-Cycles) 
# 2. [Zip Dictionary](#Zip-Dictionary)
# 3. [List Intersections](#List-Intersections)
# 4. [Find Duplicates](#Find-Duplicates)
# 5. [Sum of the Product of Key and Value](#Sum-of-the-Product-of-Key-and-Value)
# 6. [String Permutation is Palindrome](#String-Permutation-is-Palindrome)
# 7. [Letter Histogram](#Letter-Histograms)
# 8. [Reverse Dictionary](#Reverse-Dictionary)

# # Count Cycles
# ---
# Given an array of integers, find how many cycles are contained. Each element of the array indicates which index of the array should be visited next.
# For example, the array `[1,3,0,0]` contains one cycle, since element at index 0 points to index 1, which points to index 3, which points back to index 0.
# 
# ## Restriction(s):
# ---
# * Input array `arr` contains fewer than 1000 elements and at least one.
# * An element which points to its own index is considered a cycle and should be counted.
# * Each element in the array will be an integer within `[0, n-1]`, where n is the length of the array.
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `arr`: `[0,2,4,1,0]`
# 
#     * Output: 
#         * `1`  There is exactly one cycle in this array, the length-1 cycle at index 0
#   
# * Example 2:
#     * Input: 
#         * `arr`: `[1,3,5,4,0,2,7,6]`
# 
#     * Output: 
#         * `3` The cycles here are the indices $0 \rightarrow 1 \rightarrow 3 \rightarrow 4$, $2 \rightarrow 5$, and $6 \rightarrow 7$ 
# 
# ## Parameters
# -----------
# * `list` : `arr`
#     - An array of integers from 0 to the length of `arr` indicating which index to visit next
# 
# 
# ## Returns
# -------
# * `int`: Number of cycles
# 

# In[393]:

def count_cycles(arr): 
    index=0
    j=[]
    count=0
    i=0
    for i in range(len(arr)):
        index=i
        times=0
        while True:
            if arr[index]==i and index not in j:
                a=i
                for b in range(len(arr)):
                    j.append(a)
                    a=arr[a]
                count += 1
                break
            if times>len(arr):
                break
            times += 1  
            index=arr[index]
    return count
    pass


# In[394]:

def test_count_cycles():
    assert count_cycles([0,2,4,1,0])==1
    assert count_cycles([1,3,5,4,0,2,7,6])==3
    assert count_cycles([3,0,0,0])==1


# # Zip Dictionary
# ---
# Given two arrays, named `keys` and `values`, create a dictionary with keys from `keys` and values from `values`. If there are keys that are matched with more than one value, change the value linked to that key to a list of all of distinct values given by the list of values. That is, if the same key-value pair is included twice in the input, it should be included in the dictionary only once. 
# 
# ## Restriction(s):
# ---
# * Both arrays will be non-empty and will have the same length.
# * The keys in `keys` are not necessarily unique. Keys may be of different types.
# * The total number of entries in the correct dictionary will be no greater than 1,000.
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `keys`: `["Pupper","Doggo","Bork","Doge","Shiba"]`
#         * `values`: `[2,7,5,5,3]`
# 
#     * Output: 
#         * `{"Pupper":2,"Doggo":7,"Bork":5,"Doge":5,"Shiba":3}`
#   
# * Example 2:
#     * Input: 
#         * `keys`: `["Google","Apple","Microsoft","Oracle","Amazon","Cisco","Google","Yahoo"]`
#         * `values`: `[(0,0),(1,3),(3,4),(1,4),(2,-1),(1,6),(5,4),(3,9)]`
# 
#     * Output: 
#         * `{"Google":[(0,0),(5,4)],"Apple":(1,3),"Microsoft":(3,4),"Oracle":(2,-1),"Amazon":(1,6),"Yahoo":(3,9)}`
#         * Note that since `"Google"` has two values, they are placed in an array
# * Example 3:
#     * Input:
#         * `keys`: `[100,100,100,200,200,300,300]`
#         * `values`: `[125,125,173,225,233,374,374]`
#     * Output:
#         * `{100:[125,173],200:[225,233],300:374}`
#         * The duplicate values of 125 and 374 have been removed
# 
# ## Parameters
# -----------
# * `list` : `keys`
#     - An array of (not necessarily unique) keys for the dictionary
# * `list` : `values`
#     - An array of (not necessarily unique) values for the dictionary
# 
# 
# ## Returns
# -------
# * `dict`: Dictionary of key-value pairs generated from the `keys` and `values`
# 

# In[395]:

def zip_dictionary(keys, values): 
    dictionary={}
    for i in range(len(keys)):
        if keys[i] not in dictionary:
            dictionary[keys[i]] = values[i]
        else:
            if isinstance(dictionary[keys[i]],(list,tuple)):
                dictionary[keys[i]].append(values[i])
            else:
                dictionary[keys[i]]=[dictionary[keys[i]]]
                dictionary[keys[i]].append(values[i])    
    return dictionary
    pass


# In[396]:

def test_zip_dictionary():
    assert zip_dictionary(["Pupper","Doggo","Bork","Doge","Shiba"],[2,7,5,5,3])=={"Pupper":2,"Doggo":7,"Bork":5,"Doge":5,"Shiba":3}
    assert zip_dictionary(["Google","Apple","Microsoft","Oracle","Amazon","Cisco","Google","Yahoo"],[(0,0),(1,3),(3,4),(1,4),(2,-1),(1,6),(5,4),(3,9)])=={'Google': [(0, 0), (5, 4)], 'Cisco': (1, 6), 'Apple': (1, 3), 'Yahoo': (3, 9), 'Amazon': (2, -1), 'Oracle': (1, 4), 'Microsoft': (3, 4)}
    assert zip_dictionary([100,100,100,200,200,300,300],[125,125,173,225,233,374,374])=={100:[125,173],200:[225,233],300:374}


# # List Intersections
# ---
# Write a function that given two list of integers, RETURNS a list of their unique intersection. That is find A ∩ B, given list A and list B.
# 
# ## Restriction(s):
# ---
# * Your solution should not use sets or set operations.
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `[1,2,3]`
#         * `[3,2,0]`
# 
#     * Output: 
#         * `[2, 3]`
#   
# * Example 2:
#     * Input: 
#         * `[]`
#         * `[1]`
# 
#     * Output: 
#         * `[]`
#         
# 
# ## Parameters
# -----------
# * `ar1` : `List[int]`
#     * `A list of integers.`
# * `ar2` : `List[int]`
#     * `A list of integers.`
# 
# 
# ## Returns
# -------
# * `List[int]`: 
#     * `Returns a list that represents the unique intersection of the two lists.`

# In[397]:

def list_intersection(ar1, ar2):
    intersection=[]
    ar1proper=[]
    for i in range(len(ar1)):
        if not ar1[i] in ar1proper:
            ar1proper.append(ar1[i])
    for i in range(len(ar1proper)):
        if ar1proper[i] in ar2:
            intersection.append(ar1proper[i])
    return intersection
    pass


# In[398]:

def test_list_intersection():
    assert list_intersection([1,2,3], [3,2,0]) == [2, 3]
    assert list_intersection([], [1]) == []
    assert list_intersection([1, 1, 2], [1, 2]) == [1,2]


# # Find Duplicates
# ---
# Write a function a list of integers, RETURNS a list of all of its duplicates.
# 
# ## Restriction(s):
# ---
# * Your solution should not use sets or set operations.
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `[1,2]`
# 
#     * Output: 
#         * `[]`
#   
# * Example 2:
#     * Input: 
#         * `[1,2,1]`
# 
#     * Output: 
#         * `[1]`
# 
# 
# ## Parameters
# -----------
# * `ar` : `List[int]`
#     * `A list of integers.`
# 
# 
# ## Returns
# -------
# * `List[int]`: 
#     * `Returns a list that represents all the duplicates in the given list.`

# In[399]:

def find_duplicates(ar):
    duplicates=[]
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i!=j and ar[i]==ar[j]:
                if not ar[i] in duplicates: 
                    duplicates.append(ar[i])
    return duplicates
    pass


# In[400]:

def test_find_duplicates():
    assert find_duplicates([1,2]) == []
    assert find_duplicates([1,2,1]) == [1]
    assert find_duplicates([]) == []


# # Sum of the Product of Key and Value
# ---
# Given a dictionary, RETURN the sum of the products of each key-value pair.
# 
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `{1: 2, 3: 4, 5: 6}`
# 
#     * Output: 
#         * `44`
#   
# * Example 2:
#     * Input: 
#         * `{0: 1, 0: 57, 1: 0, 1: 1}`
# 
#     * Output: 
#         * `1`
# 
# 
# ## Parameters
# -----------
# * `num_dict` : `Dictionary`
#     * `A dictionary with keys and values that are both integers`
# 
# 
# ## Returns
# -------
# * `int`: 
#     * `Returns the resulting sum`

# In[401]:

def sum_of_product_of_key_and_value(num_dict):
    sum=0
    for key in num_dict:
        if isinstance(key, int) and isinstance(num_dict[key], int):
            sum += key*num_dict[key]
    return sum
    pass


# In[402]:

def test_sum_of_product_of_key_and_value():
    assert (sum_of_product_of_key_and_value({1: 2, 3: 4, 5: 6}) == 44) 
    assert (sum_of_product_of_key_and_value({0: 1, 0: 57, 1: 0, 1: 1}) == 1) 
    assert (sum_of_product_of_key_and_value({0:0}) == 0)    


# # String Permutation is Palindrome
# ---
# Given a string, determine whether or not any arangement of the characters would produce a palindrome.
# 
# ## Restriction(s):
# ---
# * Your solution should only consider alpha-numeric characters (a-z, A-Z, 0-9) and should treat lowercase and uppercase characters as being different (A =/= a).
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `abab`
# 
#     * Output: 
#         * `true`
#   
# * Example 2:
#     * Input: 
#         * `CS 196`
# 
#     * Output: 
#         * `false`
# 
# 
# ## Parameters
# -----------
# * `input` : `string`
#     * `A list of integers.`
# 
# 
# ## Returns
# -------
# * `boolean`: 
#     * `Returns a boolean value. True if a permutation of the String can be a palindrome, false otherwise.`

# In[403]:

def string_permutation_is_palindrome(input):
    dictionary={}
    for i in range(len(input)):
        if not input[i].isalnum():
            continue
        if input[i] in dictionary:
            dictionary[input[i]]+=1
        else:
            dictionary[input[i]]=1
        oddCount=0
        for key in dictionary:
            if dictionary[key]%2==1:
                oddCount+=1
    return oddCount<=1
    pass


# In[404]:

def test_string_permutation_is_palindrome():
    assert (string_permutation_is_palindrome("abab"))
    assert not (string_permutation_is_palindrome("CS 196"))
    assert not string_permutation_is_palindrome("Abab")
    assert (string_permutation_is_palindrome("race car"))


# # Letter Histograms
# ---
# Write a function that, given a string, returns a dictionary of all of the letter frequencies of the letters present in the string!
# ## Restrictions:
# ---
# 
# * E̯̟͈̔͝v͇e̫̜͈̱͆ͣr̨̡͓̔͂ͯy̵̹̟̓҉̠̙̈̚t̴̖͓ͯh̺͇̖͡i̱̪͊ͤņ̦ģ̺ ̆i̶̖̦ͫ̐͠s͏̖̍̕ ̪̱̣̌́ͪ͐͛̌͊̽̉f̟̣́̀̀͑ͭâͧí̸̭͘r̸͉̓̄̉̎ͫ͢ ̓g̸̲̝̝̫̘̅ͦa͓m͓̙̀̕ͅe̱̳͍̟ͤͬ̎̏̎͞.̩̣̅ͣ ̼̫̮̤̫̾̊ͦ̄̚҉D̹̀̾̋̊͘oņ͓̮̅͠'̥t̻ ̱̩̪̭̍ͤͩ͢͡e͎̿x͉ͣ̍̔p̙͖̽ͭ̀̔́ḛ̻҉ͫ̍ct̔ ̹̐̄̇ͅt͍̘̜̉̍͐̀͗̇̄̃h̟̳͔̏͊͘i̠̤͔͊̏s͐̈́̀̀̂̀̊ ̤̽ṭ̶͠o͊͏̣͈̃ ͗͝b̶͖͎ͫ͑͞e̞̺ͨ͆ ͋ḛa̜̬͛̐̀ͥ͘ͅs̞̭͖̼̮̚͘͟y.̳͎͂͂̊́̅͋̓͐̆
#        * Everything is fair game. 
# * Capitalization matters
# * Spaces matter
# * All utf-8 characters matter
# * All other characters also matter. 
# * Order of the keys in your dictionary don't matter.
# * **No Imports**. You don't need them. Seriously. 
# 
# # Example(s):
# ---
# Example 1:
# * Input: `'this is a really neat method, drake!'`
# * Output: `{'a': 4, ' ': 6, 'e': 4, 'd': 2, 'i': 2, 'h': 2, 'k': 1, 'm': 1, 'l': 2, 'o': 1, 'n': 1, 's': 2, 'r': 2, '!': 1, 't': 3, 'y': 1, ',': 1}`
#   
# 
# ## Parameters:
# ---
# * st: `string`:
#     * There are no real restrictions on this string.
#     * This string will not be larger than the largest unsigned integer in python. Probably. 
#     
# ## Returns:
# ---
# * dic: `dict`<`String`, `int`>
#     * Order of keys does not matter. 
#     * No Value should be less than 1. 

# In[405]:

def letter_hist(st):
    dictionary={}
    for c in st:
        if c in dictionary:
            dictionary[c]+=1
        else:
            dictionary[c]=1
    return dictionary   


# In[406]:

def test_letter_hist():
    assert letter_hist("Seems like the homework team is having a little too much fun here.") == {' ': 12, '.': 1, 'S': 1, 'a': 3, 'c': 1, 'e': 9, 'f': 1, 
                                                                                                 'g': 1, 'h': 5, 'i': 4, 'k': 2, 'l': 3, 'm': 4, 'n': 2, 'o': 4,
                                                                                                 'r': 2, 's': 2, 't': 5, 'u': 2, 'v': 1, 'w': 1}
    
    assert letter_hist('n00t n00t! ;)') == {'!': 1, ' ': 2, ')': 1, 'n': 2, '0': 4, 't': 2, ';': 1}
    assert letter_hist('Are you ready for test case #3? I know I am!') == {'!': 1, ' ': 10, '#': 1, '3': 1, '?': 1, 'A': 1, 'I': 2, 'a': 3, 'c': 1, 'e': 4, 'd': 1, 'f': 1, 'k': 1, 'm': 1, 'o': 3, 'n': 1, 's': 2, 'r': 3, 'u': 1, 't': 2, 'w': 1, 'y': 2}
    assert letter_hist("""Chief Justice Roberts, President Carter, President Clinton, President Bush, President Obama, fellow A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ns, and people of the world: thank you.

We, the citizens of A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢, are now joined in a great national effort to rebuild our country and to restore its promise for all of our people.

Together, we will determine the course of A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ and the world for years to come.

We will face challenges. We will confront hardships. But we will get the job done.

Every four years, we gather on these steps to carry out the orderly and peaceful transfer of power, and we are grateful to President Obama and First Lady Michelle Obama for their gracious aid throughout this transition. They have been magnificent.

Today’s ceremony, however, has very special meaning. Because today we are not merely transferring power from one Administration to another, or from one party to another – but we are transferring power from Washington, D.C. and giving it back to you, the A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n People.

For too long, a small group in our nation’s Capital has reaped the rewards of government while the people have borne the cost.

Washington flourished – but the people did not share in its wealth.

Politicians prospered – but the jobs left, and the factories closed.

The establishment protected itself, but not the citizens of our country.

Their victories have not been your victories; their triumphs have not been your triumphs; and while they celebrated in our nation’s Capital, there was little to celebrate for struggling families all across our land.

That all changes – starting right here, and right now, because this moment is your moment: it belongs to you.

It belongs to everyone gathered here today and everyone watching all across A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢. 

This is your day. This is your celebration.

And this, the United States of A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢, is your country.

What truly matters is not which party controls our government, but whether our government is controlled by the people.

January 20th 2017, will be remembered as the day the people became the rulers of this nation again. 

The forgotten men and women of our country will be forgotten no longer.

Everyone is listening to you now.

You came by the tens of millions to become part of a historic movement the likes of which the world has never seen before.

At the center of this movement is a crucial conviction: that a nation exists to serve its citizens.

A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ns want great schools for their children, safe neighborhoods for their families, and good jobs for themselves.

These are the just and reasonable demands of a righteous public.

But for too many of our citizens, a different reality exists: Mothers and children trapped in poverty in our inner cities; rusted-out factories scattered like tombstones across the landscape of our nation; an education system, flush with cash, but which leaves our young and beautiful students deprived of knowledge; and the crime and gangs and drugs that have stolen too many lives and robbed our country of so much unrealized potential.

This A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n carnage stops right here and stops right now.

We are one nation – and their pain is our pain.  Their dreams are our dreams; and their success will be our success.  We share one heart, one home, and one glorious destiny.

The oath of office I take today is an oath of allegiance to all A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ns.

For many decades, we’ve enriched foreign industry at the expense of A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n industry;

Subsidized the armies of other countries while allowing for the very sad depletion of our military;

We've defended other nation’s borders while refusing to defend our own;

And spent trillions of dollars overseas while A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢'s infrastructure has fallen into disrepair and decay.

We’ve made other countries rich while the wealth, strength, and confidence of our country has disappeared over the horizon.

One by one, the factories shuttered and left our shores, with not even a thought about the millions upon millions of A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n workers left behind.

The wealth of our middle class has been ripped from their homes and then redistributed across the entire world.

But that is the past. And now we are looking only to the future.

We assembled here today are issuing a new decree to be heard in every city, in every foreign capital, and in every hall of power.

From this day forward, a new vision will govern our land.

From this moment on, it’s going to be A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ First.

Every decision on trade, on taxes, on immigration, on foreign affairs, will be made to benefit A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n workers and A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n families.

We must protect our borders from the ravages of other countries making our products, stealing our companies, and destroying our jobs.  Protection will lead to great prosperity and strength.

I will fight for you with every breath in my body – and I will never, ever let you down.

A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ will start winning again, winning like never before.

We will bring back our jobs. We will bring back our borders.  We will bring back our wealth.  And we will bring back our dreams.

We will build new roads, and highways, and bridges, and airports, and tunnels, and railways all across our wonderful nation.

We will get our people off of welfare and back to work – rebuilding our country with A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n hands and A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n labor.

We will follow two simple rules: Buy A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n and Hire A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n.

We will seek friendship and goodwill with the nations of the world – but we do so with the understanding that it is the right of all nations to put their own interests first.

We do not seek to impose our way of life on anyone, but rather to let it shine as an example for everyone to follow.

We will reinforce old alliances and form new ones – and unite the civilized world against Radical Islamic Terrorism, which we will eradicate completely from the face of the Earth.

At the bedrock of our politics will be a total allegiance to the United States of A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢, and through our loyalty to our country, we will rediscover our loyalty to each other.

When you open your heart to patriotism, there is no room for prejudice.

The Bible tells us, “how good and pleasant it is when God’s people live together in unity.”

We must speak our minds openly, debate our disagreements honestly, but always pursue solidarity.

When A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ is united, A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ is totally unstoppable.

There should be no fear – we are protected, and we will always be protected.

We will be protected by the great men and women of our military and law enforcement and, most importantly, we are protected by God.

Finally, we must think big and dream even bigger.

In A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢, we understand that a nation is only living as long as it is striving.

We will no longer accept politicians who are all talk and no action – constantly complaining but never doing anything about it.

The time for empty talk is over.

Now arrives the hour of action.

Do not let anyone tell you it cannot be done.  No challenge can match the heart and fight and spirit of A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢.

We will not fail. Our country will thrive and prosper again.

We stand at the birth of a new millennium, ready to unlock the mysteries of space, to free the Earth from the miseries of disease, and to harness the energies, industries and technologies of tomorrow.

A new national pride will stir our souls, lift our sights, and heal our divisions.

It is time to remember that old wisdom our soldiers will never forget: that whether we are black or brown or white, we all bleed the same red blood of patriots, we all enjoy the same glorious freedoms, and we all salute the same great A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n Flag.

And whether a child is born in the urban sprawl of Detroit or the windswept plains of Nebraska, they look up at the same night sky, they fill their heart with the same dreams, and they are infused with the breath of life by the same almighty Creator.

So to all A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ns, in every city near and far, small and large, from mountain to mountain, and from ocean to ocean, hear these words:

You will never be ignored again.

Your voice, your hopes, and your dreams, will define our A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢n destiny. And your courage and goodness and love will forever guide us along the way.

Together, We Will Make A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ Strong Again.

We Will Make A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ Wealthy Again.

We Will Make A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ Proud Again.

We Will Make A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ Safe Again.

And, Yes, Together, We Will Make A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢ Great Again. Thank you, God Bless You, And God Bless A̶̰̯̬͙̰͙̘̲͌͋̎ͫ̒̉̔̄̆ͧ͘͝m̶̶͍̫̤̖͛̐̕͟e̶̶̟͙̯̤͕͋ͨ̔͋ͩ́́͒́ͫ͛ͩr̶̴̡̝̦̩̫͇͚̥̯̞̉ͮͦ͊̇ͤ͂ͣ̃ͤ̈́̚͝i̶̵͕͉̼͈̞̽͋́̀̒͂́ͧ̈̀͢c̶̛͖̖̓ͯ̍ͧ͗ͬ͞a̶̛̲͎̯̺̥̻ͧ̽̂ͧ̈́͢.""") == {'\n': 148,
 ' ': 1377,
 "'": 2,
 ',': 95,
 '-': 1,
 '.': 89,
 '0': 2,
 '1': 1,
 '2': 2,
 '7': 1,
 ':': 7,
 ';': 9,
 'A': 51,
 'B': 9,
 'C': 7,
 'D': 3,
 'E': 5,
 'F': 8,
 'G': 5,
 'H': 1,
 'I': 7,
 'J': 2,
 'L': 1,
 'M': 7,
 'N': 3,
 'O': 5,
 'P': 9,
 'R': 2,
 'S': 6,
 'T': 21,
 'U': 2,
 'W': 39,
 'Y': 5,
 'a': 486,
 'b': 104,
 'c': 179,
 'd': 248,
 'e': 807,
 'f': 147,
 'g': 129,
 'h': 271,
 'i': 474,
 'j': 9,
 'k': 35,
 'l': 326,
 'm': 159,
 'n': 467,
 'o': 557,
 'p': 102,
 'r': 506,
 's': 354,
 't': 532,
 'u': 189,
 'v': 63,
 'w': 146,
 'x': 5,
 'y': 123,
 'z': 8,
 '̀': 68,
 '́': 34,
 '̂': 34,
 '̃': 34,
 '̄': 34,
 '̆': 34,
 '̇': 34,
 '̈': 34,
 '̉': 68,
 '̍': 34,
 '̎': 34,
 '̐': 34,
 '̒': 68,
 '̓': 34,
 '̔': 68,
 '̕': 34,
 '̖': 68,
 '̘': 34,
 '̚': 34,
 '̛': 68,
 '̝': 34,
 '̞': 68,
 '̟': 34,
 '̡': 34,
 '̤': 68,
 '̥': 68,
 '̦': 34,
 '̩': 34,
 '̫': 68,
 '̬': 34,
 '̯': 136,
 '̰': 68,
 '̲': 68,
 '̴': 34,
 '̵': 34,
 '̶': 306,
 '̺': 34,
 '̻': 34,
 '̼': 34,
 '̽': 68,
 '́': 136,
 '͂': 68,
 '̈́': 68,
 '͇': 34,
 '͈': 34,
 '͉': 34,
 '͊': 34,
 '͋': 136,
 '͌': 34,
 '͍': 34,
 '͎': 34,
 '͒': 34,
 '͕': 68,
 '͖': 34,
 '͗': 34,
 '͘': 34,
 '͙': 102,
 '͚': 34,
 '͛': 68,
 '͝': 68,
 '͞': 34,
 '͟': 34,
 '͢': 68,
 'ͣ': 34,
 'ͤ': 68,
 'ͦ': 34,
 'ͧ': 170,
 'ͨ': 34,
 'ͩ': 68,
 'ͫ': 68,
 'ͬ': 34,
 'ͮ': 34,
 'ͯ': 34,
 '–': 11,
 '’': 8,
 '“': 1,
 '”': 1}


# # Reverse Dictionary
# ---
# For this method, given any dictionary, you need to reverse the keys and values. Since there can be multiple keys that map to the same value, have all values on a given key be stored in a set in the dictionary you return.
# 
# ## Example(s):
# ---
# Example 1:
# * `{'a':'b', 'c':'b', 'd': 'x'}`
# * `{'b': set(['a', 'c']),  'x':set(['d'])}`.
# This can also be represented as `{'b':{'a','c'}, 'x':{'d'}}` depending on where you're running your code. 
# 
# ## Restriction(s):
# ---
# * **No Imports**. You still don't need them. Seriously.
# * Everything that will be in a dictionary that is given to you will be hashable. No bamboozle. 
# * You can expect somewhat less than 9223372036854775807 key-value pairs. 
#   
# ## Parameters: 
# ---
# * dic: `{A: B}` 
#     * Where `A` and `B` are hashable types.  
# 
# ## Output:
# ---
# * out_dic: `{A: set([B])}`
#     * Where `A` and `B` are the same types as the input. 

# In[407]:

def reverse_dict(dic):
    dic2={}
    for key in dic:
        if dic[key] in dic2:
            dic2[dic[key]].add(key)
        else:
            dic2[dic[key]]=set(key)
    return dic2
    pass


# In[413]:

def test_reverse_dict():
    assert reverse_dict({'a':'b', 'b':'b', 'c':'d'}) == {'b': {'a', 'b'}, 'd': {'c'}}
    assert reverse_dict({'a':'b', 'b':'c', 'c':'d', 'd':'e','e':'f'}) == {'b': {'a'}, 'c': {'b'}, 'd': {'c'}, 'e': {'d'}, 'f': {'e'}}


# In[414]:

def test_all():
    # Add your test case here. This should be at the very end
    test_count_cycles()
    test_list_intersection()
    test_find_duplicates()
    test_sum_of_product_of_key_and_value()
    test_string_permutation_is_palindrome()
    test_letter_hist()
    test_reverse_dict()


# In[415]:

test_all()

