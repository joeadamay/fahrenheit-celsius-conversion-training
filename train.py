# To convert from Fahrenheit to Celsius, follow this formula:
# C = (F - 32) * 5 / 9
#
# Thus, these operations need to be learned:
# x - 32,
# x * 5, and
# x / 9,
# the final two of which can be helped by memorizing multiples of 5 and 9.

import random

# Return a pseudorandom tuple of form (TYPE, PROB_VAL, ANS),
# where TYPE is one of
#   0: x - 32 = ?
#   1: x * 5 = ?
#   2: x / 9 = ?
#   3: xF -> ?C (full unit conversion),
# PROB_VAL is x in the above problem examples, and
# ANS is the answer.
#
# This function produces problems that help in the range of
# -148F to 212F, or
# -100C to 100C
def get_problem(is_full_conversion):
    min_f = -148
    max_f = 212

    problem_type = random.randrange(3) if not is_full_conversion else 3
    problem_value = 0
    answer = 0

    if 0 == problem_type:
        problem_value = random.randrange(min_f, max_f + 1)
        answer = problem_value - 32
    elif 1 == problem_type:
        # Assume that this is the final step, i.e. that the value has already
        # been evenly divided by 9
        problem_value = random.randrange(min_f - 32, max_f - 32 + 1, 9) / 9
        answer = problem_value * 5
    elif 2 == problem_type:
        # Only use values that give integral answers
        problem_value = random.randrange(min_f - 32, max_f - 32 + 1, 9)
        answer = problem_value / 9
    elif 3 == problem_type:
        # Only use values that give integral answers
        problem_value = random.randrange(min_f, max_f + 1, 9)
        answer = (problem_value - 32) * 5 / 9

    return (int(problem_type), int(problem_value), int(answer))


# Returns either 'quit' or an integer
def get_input(question):
    user_input = ''
    while True:
        user_input = input(question).lower()
        if 'quit' == user_input:
            break;
        try:
            user_input = int(user_input)
            break
        except:
            print('Please enter an integer or enter "quit" to exit.')

    return user_input


# Train on the 3 component calculations used in the conversion:
#   x - 32
#   x * 5
#   x / 9
def train(is_full_conversion):
    question = ''
    user_input = ''
    user_value = 0

    running = True
    while running:
        (prob_type, prob_value, prob_answer) = get_problem(is_full_conversion)

        # Make quesiton
        if 0 == prob_type:
            question = f'{prob_value} - 32 = '
        elif 1 == prob_type:
            question = f'{prob_value} * 5 = '
        elif 2 == prob_type:
            question = f'{prob_value} / 9 = '
        elif 3 == prob_type:
            question = f'Convert {prob_value} from Fahrenheit to Celsius: '

        while True:
            user_input = get_input(question)

            if 'quit' == user_input:
                # Exit program
                running = False
                break
            elif prob_answer == user_input:
                # Get a new problem
                print("Correct!\n")
                break
            else:
                # Retry the same problem
                print("Try again.")


if __name__ == '__main__':
    # Choose component calculations or full conversion
    is_full_conversion = False
    while True:
        print('Modes:')
        print('  1: Component Calculations')
        print('     Train on simple calculations to help with doing the full conversion from Fahrenheit to Celsius.')
        print('  2: Full Unit Conversion')
        print('     Convert from Fahrenheit to Celsius.')
        print()

        user_input = input('Select a mode: ').lower()

        try:
            user_input = int(user_input)
        except:
            user_input = -1

        if 1 == user_input:
            is_full_conversion = False
            break
        elif 2 == user_input:
            is_full_conversion = True
            break
        else:
            print('Please enter a valid option ("1" or "2").\n')

    train(is_full_conversion)
