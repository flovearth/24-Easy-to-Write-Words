

left_hand_set = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
right_hand_set = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm', 'ğ', 'ü', 'ş', 'ö', 'ç', 'ı'}
word = input('what\'s Your Word: ')
word = word.lower()
given_word_set = set(word)  # given word returned to a set

a = (left_hand_set.union(given_word_set))  # union of both
b = (right_hand_set.union(given_word_set))

left_hand_usage = (len(a) > len(left_hand_set))  # if the union of two sets 
                                                # bigger than the set itself it turns to 
                                                # True means left hand used.
right_hand_usage = (len(b) > len(right_hand_set))

result = (left_hand_usage and right_hand_usage)  # both True means both hands used.

if result:
    print('This word is easy to write. (You use both hands.)')
else:
    print('This word is not easy to write. You have to use one hand only.')