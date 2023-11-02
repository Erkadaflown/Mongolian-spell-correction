import textdistance
import pickle

with open('model/correction_model.pkl', 'rb') as model_file:
    correction_dict = pickle.load(model_file)

def predict_correction(incorrect_word, correction_dict):
    if incorrect_word in correction_dict:
        return correction_dict[incorrect_word], 0  
    else:
        best_match = None
        best_distance = float('inf') 

        for correct_word in correction_dict.keys():
            distance = textdistance.levenshtein(incorrect_word, correct_word)
            if distance < best_distance:
                best_distance = distance
                best_match = correct_word

        return best_match, best_distance

def correct_text(input_text, correction_dict):
    corrected_text = []
    words = input_text.split()

    for word in words:
        best_correction, distance = predict_correction(word, correction_dict)
        if best_correction:
            corrected_text.append(best_correction)
        else:
            corrected_text.append(word) 

    return ' '.join(corrected_text)



def wordmain (input):

    input_text = input 
    corrected_text = correct_text(input_text, correction_dict)
    return corrected_text