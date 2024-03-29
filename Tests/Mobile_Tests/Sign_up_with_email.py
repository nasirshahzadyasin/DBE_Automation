import csv
import pytest
from Pages.Mobile_pages.OnboardingPage import OnboardingPage


@pytest.mark.csv
def test_signup_with_email():
    signUp = OnboardingPage()
    if signUp.Get_started():
        get_started_btn_clicked_status = 'Pass'
        log_test_result("Verify that Get Started btn should be tapped successfully ",
                        get_started_btn_clicked_status)
        # Onboarding screen 1
        if signUp.Onboarding_arrow_1():
            onboarding_arrow_1_status = 'Pass'
            log_test_result("Verify that onboarding_arrow_1 should be tapped successfully",
                            onboarding_arrow_1_status)

            # Onboarding screen 2
            if signUp.Onboarding_arrow_2():
                onboarding_arrow_2_status = 'Pass'
                log_test_result("Verify that onboarding_arrow_2 should be tapped successfully",
                                onboarding_arrow_2_status)
                # Onboarding screen 3
                if signUp.Onboarding_arrow_3():
                    onboarding_arrow_3_status = 'Pass'
                    log_test_result("Verify that onboarding_arrow_3 should be tapped successfully",
                                    onboarding_arrow_3_status)

                    if signUp.onboarding_get_started():
                        onboarding_get_started_btn_status = 'Pass'
                        log_test_result("Verify that onboarding_get_started_btn should be tapped successfully",
                                        onboarding_get_started_btn_status)

                        if signUp.sign_up_with_email():
                            sign_up_with_email = 'Pass'
                            log_test_result("Verify that sign_up_with_email button should be tapped successfully",
                                            sign_up_with_email)

                            if signUp.input_email():
                                email_input_status = 'Pass'
                                log_test_result("Verify that user email should be entered successfully",
                                                email_input_status)

                                if signUp.input_fname():
                                    first_name_input_status = 'Pass'
                                    log_test_result("Verify that user should be able to enter first name successfully",
                                                    first_name_input_status)

                                    if signUp.input_lname():
                                        last_name_input_status = 'Pass'
                                        log_test_result(
                                            "Verify that user should be able to enter last name successfully",
                                            last_name_input_status)

                                        if signUp.input_password():
                                            password_input_status = 'Pass'
                                            log_test_result(
                                                "Verify that user should be able to enter password successfully",
                                                password_input_status)
                                            if signUp.input_retype_password():
                                                confirm_password_status = 'Pass'
                                                log_test_result(
                                                    "Verify that user should be able to confirm password successfully",
                                                    confirm_password_status)
                                                # sign up button
                                                if signUp.sign_up_btn():
                                                    signup_button_status = 'Pass'
                                                    log_test_result(
                                                        "Verify that signup button should be tapped and account should be created "
                                                        "successfully",
                                                        signup_button_status)
                                                    if signUp.notif_allow_link():
                                                        notif_allow_link_status = 'Pass'
                                                        log_test_result(
                                                            "Verify that user should be able to enter last name successfully",
                                                            notif_allow_link_status)

                                                        if signUp.sprout_tooltip():
                                                            sprout_tooltip_status = 'Pass'
                                                            log_test_result(
                                                                "Verify that user should be able to enter password successfully",
                                                                sprout_tooltip_status)
                                                            if signUp.compost_tooltip():
                                                                compost_tooltip_status = 'Pass'
                                                                log_test_result(
                                                                    "Verify that user should be able to confirm password successfully",
                                                                    compost_tooltip_status)
                                                                # sign up button
                                                                if signUp.ewaste_tooltip():
                                                                    ewaste_tooltip_status = 'Pass'
                                                                    log_test_result(
                                                                        "Verify that signup button should be tapped and account should be created "
                                                                        "successfully",
                                                                        ewaste_tooltip_status)

                                                                else:
                                                                    ewaste_tooltip_status = 'Fail'
                                                                    # Log the test result to CSV
                                                                    log_test_result(
                                                                        "Verify that signup button should be tapped and account should be created successfully",
                                                                        ewaste_tooltip_status)

                                                            else:
                                                                compost_tooltip_status = 'Fail'
                                                                # Log the test result to CSV
                                                                log_test_result(
                                                                    "Verify that user should be able to confirm password successfully",
                                                                    compost_tooltip_status)
                                                        else:
                                                            sprout_tooltip_status = 'Fail'
                                                            # Log the test result to CSV
                                                            log_test_result(
                                                                "Verify that user should be able to enter password successfully",
                                                                sprout_tooltip_status)
                                                    else:
                                                        notif_allow_link_status = 'Fail'
                                                        # Log the test result to CSV
                                                        log_test_result(
                                                            "Verify that user should be able to enter last name successfully",
                                                            notif_allow_link_status)

                                                else:
                                                    signup_button_status = 'Fail'
                                                    # Log the test result to CSV
                                                    log_test_result(
                                                        "Verify that signup button should be tapped and account should be created successfully",
                                                        signup_button_status)

                                            else:
                                                confirm_password_status = 'Fail'
                                                # Log the test result to CSV
                                                log_test_result(
                                                    "Verify that user should be able to confirm password successfully",
                                                    confirm_password_status)
                                        else:
                                            password_input_status = 'Fail'
                                            # Log the test result to CSV
                                            log_test_result(
                                                "Verify that user should be able to enter password successfully",
                                                password_input_status)
                                    else:
                                        last_name_input_status = 'Fail'
                                        # Log the test result to CSV
                                        log_test_result(
                                            "Verify that user should be able to enter last name successfully",
                                            last_name_input_status)

                                else:
                                    first_name_input_status = 'Fail'
                                    log_test_result("Verify that user should be able to enter first name successfully",
                                                    first_name_input_status)

                            else:
                                email_input_status = 'Fail'
                                # Log the test result to CSV
                                log_test_result("Verify that user email should be entered successfully",
                                                email_input_status)

                        else:
                            sign_up_with_email = 'Fail'
                            # Log the test result to CSV
                            log_test_result("Verify that sign_up_with_email button should be tapped successfully",
                                            sign_up_with_email)

                    else:
                        onboarding_get_started_btn_status = 'Fail'
                        log_test_result("Verify that onboarding_get_started_btn should be tapped successfully",
                                        onboarding_get_started_btn_status)

                else:
                    onboarding_arrow_3_status = 'Fail'
                    log_test_result("Verify that onboarding_arrow_3 should be tapped successfully",
                                    onboarding_arrow_3_status)
            else:
                onboarding_arrow_2_status = 'Fail'
                log_test_result("Verify that onboarding_arrow_2 should be tapped successfully",
                                onboarding_arrow_2_status)

        else:
            onboarding_arrow_1_status = 'Fail'
            log_test_result("Verify that onboarding_arrow_t should be tapped successfully",
                            onboarding_arrow_1_status)

    else:
        get_started_btn_clicked_status = 'Fail'
        log_test_result("Verify that Get Started button should be tapped successfully ",
                        get_started_btn_clicked_status)


def log_test_result(test_name, status):
    csv_file = "Results/Sign_with_email.csv"
    csv_headers = ["Signup Tests Steps", "Status"]
    csv_rows = [{"Signup Tests Steps": test_name, "Status": status}]  # Wrapping rows in a list of dictionaries

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)

        # Check if the file is empty to write the header
        if file.tell() == 0:
            writer.writeheader()

        writer.writerows(csv_rows)


if __name__ == "__main__":
    pytest.main()
