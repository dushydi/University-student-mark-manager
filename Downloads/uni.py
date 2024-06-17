valid_credit = [0, 20, 40, 60, 80, 100, 120]  # list of valid credits
exclude_list = [120, 80, 100]  # credit at fail values
do_not_progress_list = [0, 20, 40, 60, 80, 100, 120]  # credit at defer values
progress_module_trailer2 = [100]  # credit at pass values
results_given = 0  # To store total results given as output to the user
progress_total = 0  # To store total progress outcomes
trailer_total = 0  # To store total trailer outcomes
retriever_total = 0  # To store total retriever outcomes
exclude_total = 0  # To store total exclude outcomes
final_result_list = []  # List to store the final result list for part 2


def student()

    while True:
        try:
            pass_credit = int(input("Please enter your credits at pass: "))
            if pass_credit not in valid_credit:  # to check if the entered values are in valid
                print("Out of range")
            else:
                defer_credit = int(input("Please enter your credit at defer: "))
                if defer_credit not in valid_credit:
                    print("Out of range")
                else:
                    fail_credit = int(input("Please enter your credit at fail: "))
                    if fail_credit not in valid_credit:
                        print("Out of range")

                    total_credit = pass_credit + defer_credit + fail_credit
                    if total_credit != 120:#to check if the total of entered  values are valid
                        print("Total incorrect")
                    else:
                        # 1
                        if pass_credit == 120:
                            print("Progress")
                        # 2
                        elif fail_credit in exclude_list:
                            print("Exclude")
                        # 3
                        elif pass_credit in progress_module_trailer2:
                            print("Progress (module trailer)")
                        # 4
                        elif defer_credit in do_not_progress_list:
                            print("Do not progress – module retriever")

                        break  # Exit the loop if input is valid

        except ValueError:
            print("Integer required. ")


def listextension(a, b):
    b_string = ', '.join(map(str, b))  # Convert the list elements to strings and join them
    return f"{a} - {b_string}"  # Concatenate the result without square brackets


while True: #to identify if the user is a student or a teacher 
    try:
        user = int(input("Enter '1' if you are a student, Enter '2' if you are a teacher: "))
        if user not in [1, 2]:
            print("Please enter only 1 or 2.")
            continue
        break
    except ValueError:
        print("Please enter 1 or 2.")

if user == 1: #only 1 outcome for a student
    student()

if user == 2: #multiple outcomes for a teacher
    while True:
        defer_credit = 0
        fail_credit = 0
        total_credit = 0
        result_list = []  # to store the inputs given by the user

        pass_credit = input("Please enter your credits at pass (enter 'q' to quit): ")

        if pass_credit.lower() == 'q':  # to make letter lowercase if the user entered uppercase q
            break

        try:
            pass_credit = int(pass_credit)  # to convert the data type of pass_credit
            if pass_credit not in valid_credit:  # to check if the entered values are in valid
                print("Out of range")
            else:
                defer_credit = int(input("Please enter your credit at defer: "))
                result_list.append(int(pass_credit))
                result_list.append(int(defer_credit))

                if defer_credit not in valid_credit:
                    print("Out of range")
                else:
                    fail_credit = int(input("Please enter your credit at fail: "))
                    result_list.append(int(fail_credit))
                    if fail_credit not in valid_credit:
                        print("Out of range")
                    else:
                        total_credit = total_credit + (pass_credit + defer_credit + fail_credit)

                        if total_credit > 120 or total_credit < 120:  # to check if the total of entered data is valid
                            print("Total incorrect")
                        # 1
                        elif pass_credit == 120:
                            print("Progress")
                            result = "progress"
                            results_given = results_given + 1
                            progress_total = progress_total + 1
                            calling_function = listextension(result, result_list)
                            final_result_list.append(calling_function)
                        # 2
                        elif fail_credit in exclude_list:
                            print("Exclude")
                            result = "Exclude"
                            results_given = results_given + 1
                            exclude_total = exclude_total + 1
                            calling_function = listextension(result, result_list)
                            final_result_list.append(calling_function)
                        # 3
                        elif pass_credit in progress_module_trailer2:
                            print("Progress (module trailer)")
                            result = "Progress (module trailer)"
                            results_given = results_given + 1
                            trailer_total = trailer_total + 1
                            calling_function = listextension(result, result_list)
                            final_result_list.append(calling_function)
                        # 4
                        elif defer_credit in do_not_progress_list:
                            print("Do not progress – module retriever")
                            result = "Do not progress – module retriever"
                            results_given = results_given + 1
                            retriever_total = retriever_total + 1
                            calling_function = listextension(result, result_list)
                            final_result_list.append(calling_function)

        except ValueError:  # runs if the user entered a non-integer
            print("Integer required  ")

# Skip the histogram when the user enters 1
if user == 2:
    from graphics import *

    def histogram_result():
        win = GraphWin("Histogram", 550, 550)
        win.setBackground(color_rgb(240, 255, 240))

        ln = Line(Point(20, 450), Point(490, 450))
        ln.setOutline("black")
        ln.setWidth(1)
        ln.draw(win)

        txt = Text(Point(100, 20), "Histogram Results")
        txt.setTextColor(color_rgb(165, 42, 42))
        txt.setSize(15)
        txt.draw(win)

        txt2 = Text(Point(100, 540), str(results_given) + "  Outcomes in total")
        txt2.setTextColor(color_rgb(100, 140, 170))
        txt2.setSize(15)
        txt2.draw(win)

        if progress_total != 0:  # to make the progress bar if progress total is not equal to 0

            bar_height1 = 400 // progress_total
            bar1 = Rectangle(Point(20, bar_height1), Point(120, 450))
            bar1.setFill(color_rgb(144, 238, 144))
            bar1.draw(win)

            text3 = Text(Point(65, bar_height1 - 10), str(progress_total))
            text3.setTextColor(color_rgb(100, 140, 170))
            text3.setSize(15)
            text3.draw(win)

            text6 = Text(Point(65, 470), "Progress")
            text6.setTextColor(color_rgb(100, 140, 170))
            text6.setSize(15)
            text6.draw(win)

        else:  # To make the progress bar if progress total is 0

            bar1 = Rectangle(Point(20, 445), Point(120, 450))
            bar1.setFill(color_rgb(144, 238, 144))
            bar1.draw(win)
            bar_height1 = 50 * progress_total

            text3 = Text(Point(65, 430), str(progress_total))
            text3.setTextColor(color_rgb(100, 140, 170))
            text3.setSize(15)
            text3.draw(win)

            text6 = Text(Point(65, 470), "Progress")
            text6.setTextColor(color_rgb(100, 140, 170))
            text6.setSize(15)
            text6.draw(win)

        if trailer_total != 0:  # to make the trailer bar if trailer total is not equal to 0

            bar_height2 = 400 // trailer_total
            bar2 = Rectangle(Point(150, bar_height2), Point(250, 450))
            bar2.setFill(color_rgb(173, 255, 173))
            bar2.draw(win)

            text7 = Text(Point(195, 470), "Trailer")
            text7.setTextColor(color_rgb(100, 140, 170))
            text7.setSize(15)
            text7.draw(win)

            text4 = Text(Point(195, bar_height2 - 10), str(trailer_total))
            text4.setTextColor(color_rgb(100, 140, 170))
            text4.setSize(15)
            text4.draw(win)

        else:  # to make the trailer bar if the trailer total is equal to 0

            bar2 = Rectangle(Point(150, 445), Point(250, 450))
            bar2.setFill(color_rgb(173, 255, 173))
            bar2.draw(win)
            bar_height2 = 50 * trailer_total

            text7 = Text(Point(195, 470), "Trailer")
            text7.setTextColor(color_rgb(100, 140, 170))
            text7.setSize(15)
            text7.draw(win)

            text4 = Text(Point(195, 430), str(trailer_total))
            text4.setTextColor(color_rgb(100, 140, 170))
            text4.setSize(15)
            text4.draw(win)

        if retriever_total != 0:  # to make the retriever bar if retriever total is not equal to 0

            bar_height3 = 400 // retriever_total
            bar3 = Rectangle(Point(280, bar_height3), Point(380, 450))
            bar3.setFill(color_rgb(200, 255, 200))
            bar3.draw(win)

            text8 = Text(Point(330, 470), "Retriever")
            text8.setTextColor(color_rgb(100, 140, 170))
            text8.setSize(15)
            text8.draw(win)

            text4 = Text(Point(330, bar_height3 - 10), str(retriever_total))
            text4.setTextColor(color_rgb(100, 140, 17))
            text4.setSize(15)
            text4.draw(win)

        else:  # to make the retriever bar if retriever total is equal to 0

            bar3 = Rectangle(Point(280, 445), Point(380, 450))
            bar3.setFill(color_rgb(200, 255, 200))
            bar3.draw(win)
            bar_height3 = 50 * retriever_total

            text4 = Text(Point(330, 430), str(retriever_total))
            text4.setTextColor(color_rgb(100, 140, 170))
            text4.setSize(15)
            text4.draw(win)

            text8 = Text(Point(330, 470), "Retriever")
            text8.setTextColor(color_rgb(100, 140, 170))
            text8.setSize(15)
            text8.draw(win)

        if exclude_total != 0:  # to make the exclude bar if exclude total is not equal to 0

            bar_height4 = 400 // exclude_total
            bar4 = Rectangle(Point(410, bar_height4), Point(508, 450))
            bar4.setFill(color_rgb(255, 182, 183))
            bar4.draw(win)

            text5 = Text(Point(465, bar_height4 - 10), str(exclude_total))
            text5.setTextColor(color_rgb(100, 140, 170))
            text5.setSize(15)
            text5.draw(win)

            text9 = Text(Point(465, 470), "Exclude")
            text9.setTextColor(color_rgb(100, 140, 170))
            text9.setSize(15)
            text9.draw(win)

        else:  # to make the exclude bar if exclude total is equal to 0

            bar4 = Rectangle(Point(410, 445), Point(508, 450))
            bar4.setFill(color_rgb(255, 182, 183))
            bar4.draw(win)
            bar_height4 = 50 * exclude_total

            text5 = Text(Point(465, 430), str(exclude_total))
            text5.setTextColor(color_rgb(100, 140, 170))
            text5.setSize(15)
            text5.draw(win)
            text9 = Text(Point(465, 470), "Exclude")
            text9.setTextColor(color_rgb(100, 140, 170))
            text9.setSize(15)
            text9.draw(win)
            win.getMouse()
            win.close()

    histogram_result()

# Print all results at the end
if user == 2:
    print("\npart 2:")
    for result in final_result_list:
        print(result)

# To print the part 2 result in a text file called "results.txt"
if user == 2:
    with open('results.txt', 'w') as file:
        file.write("Part 3:\n")
        for result in final_result_list:
            file.write(result + '\n')

    f1 = open('results.txt', 'r') #to read the text file and print them
    results = f1.read()
    f1.close
    print(results)
