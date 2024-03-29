import pytest
from Pages.Mobile_pages.eWest_page.EwastePage import EwastePage
import csv


@pytest.mark.csv
def test_Ewaste():
    ew = EwastePage()
    if ew.ewaste_action_btn():
        ewaste_action_btn_status = 'Pass'
        log_test_result("Verify that Ewaste action button should be tapped successfully",
                        ewaste_action_btn_status)
        if ew.ewaste_no_btn():
            ewaste_no_btn_status = 'Pass'
            log_test_result("Verify that Ewaste NO button should be tapped successfully ", ewaste_no_btn_status)
            if ew.ewaste_no_arrow():
                ewaste_no_arrow_status = 'Pass'
                log_test_result("Verify that Ewaste NO flow arrow  should be tapped successfully",
                                ewaste_no_arrow_status)
                if ew.ewaste_action_btn_not_sure():
                    ewaste_action_btn_not_sure_status = 'Pass'
                    log_test_result("Verify that Ewaste action button should be tapped again",
                                    ewaste_action_btn_not_sure_status)

                    if ew.ewaste_not_sure_btn():
                        ewaste_not_sure_btn_status = 'Pass'
                        log_test_result("Verify that ewaste_not_sure_btn should be tapped successful",
                                        ewaste_not_sure_btn_status)
                        if ew.ewaste_not_sure_back_arrow():
                            ewaste_not_sure_back_arrow_status = 'Pass'
                            log_test_result("Verify that ewaste_not_sure_back_arrow should be tapped successful",
                                            ewaste_not_sure_back_arrow_status)
                            if ew.ewaste_yes_btn():
                                ewaste_yes_btn_status = 'Pass'
                                log_test_result("Verify that ewaste_yes_btn should be tapped successful",
                                                ewaste_yes_btn_status)
                                if ew.ewaste_yes_arrow():
                                    ewaste_yes_arrow_status = 'Pass'
                                    log_test_result("Verify that ewaste_yes_arrow should be tapped successful",
                                                    ewaste_yes_arrow_status)
                                    if ew.ewaste_map_link():
                                        ewaste_map_link_status = 'Pass'
                                        log_test_result("Verify that ewaste_map_link should be tapped successful",
                                                        ewaste_map_link_status)
                                        if ew.ewaste_map_details_cross():
                                            ewaste_map_details_cross_status = 'Pass'
                                            log_test_result(
                                                "Verify that ewaste_map_details_cross should be tapped successful",
                                                ewaste_map_details_cross_status)
                                            if ew.ewaste_photo_cap_btn():
                                                ewaste_photo_cap_btn_status = 'Pass'
                                                log_test_result(
                                                    "Verify that ewaste_photo_cap_btn should be tapped successful",
                                                    ewaste_photo_cap_btn_status)
                                                if ew.ewaste_camera_btn():
                                                    ewaste_camera_btn_status = 'Pass'
                                                    log_test_result(
                                                        "Verify that ewaste_camera_btn should be tapped successful",
                                                        ewaste_camera_btn_status)
                                                    if ew.ewaste_camera_permission():
                                                        ewaste_camera_permission_status = 'Pass'
                                                        log_test_result(
                                                            "Verify that ewaste_camera_permission should be tapped successful",
                                                            ewaste_camera_permission_status)
                                                        if ew.ewaste_camera_capture():
                                                            ewaste_camera_capture_status = 'Pass'
                                                            log_test_result(
                                                                "Verify that ewaste_camera_capture should be tapped successful",
                                                                ewaste_camera_capture_status)
                                                            if ew.save_ok_photo():
                                                                save_ok_photo_status = 'Pass'
                                                                log_test_result(
                                                                    "Verify that save_ok_photo should be tapped successful",
                                                                    save_ok_photo_status)
                                                                if ew.verify_complete_btn():
                                                                    verify_complete_btn_status = 'Pass'
                                                                    log_test_result(
                                                                        "Verify that verify_complete_btn should be tapped successful",
                                                                        verify_complete_btn_status)
                                                                    if ew.completed_action_btn():
                                                                        completed_action_btn_status = 'Pass'
                                                                        log_test_result(
                                                                            "Verify that completed_action_btn should be tapped successful",
                                                                            completed_action_btn_status)

                                                                    else:
                                                                        completed_action_btn_status = 'Fail'
                                                                        log_test_result(
                                                                            "Verify that completed_action_btn should be tapped successful",
                                                                            completed_action_btn_status)

                                                                else:
                                                                    verify_complete_btn_status = 'Fail'
                                                                    log_test_result(
                                                                        "Verify that verify_complete_btn should be tapped successful",
                                                                        verify_complete_btn_status)

                                                            else:
                                                                save_ok_photo_status = 'Fail'
                                                                log_test_result(
                                                                    "Verify that save_ok_photo should be tapped successful",
                                                                    save_ok_photo_status)

                                                        else:
                                                            ewaste_camera_capture_status = 'Fail'
                                                            log_test_result(
                                                                "Verify that ewaste_camera_capture should be tapped successful",
                                                                ewaste_camera_capture_status)

                                                    else:
                                                        ewaste_camera_permission_status = 'Fail'
                                                        log_test_result(
                                                            "Verify that ewaste_camera_permission should be tapped successful",
                                                            ewaste_camera_permission_status)

                                                else:
                                                    ewaste_camera_btn_status = 'Fail'
                                                    log_test_result(
                                                        "Verify that ewaste_camera_btn should be tapped successful",
                                                        ewaste_camera_btn_status)

                                            else:
                                                ewaste_photo_cap_btn_status = 'Fail'
                                                log_test_result(
                                                    "Verify that ewaste_photo_cap_btn should be tapped successful",
                                                    ewaste_photo_cap_btn_status)

                                        else:
                                            ewaste_map_details_cross_status = 'Fail'
                                            log_test_result(
                                                "Verify that ewaste_map_details_cross should be tapped successful",
                                                ewaste_map_details_cross_status)

                                    else:
                                        ewaste_map_link_status = 'Fail'
                                        log_test_result("Verify that ewaste_map_link should be tapped successful",
                                                        ewaste_map_link_status)

                                else:
                                    ewaste_yes_arrow_status = 'Fail'
                                    log_test_result("Verify that ewaste_yes_arrow should be tapped successful",
                                                    ewaste_yes_arrow_status)

                            else:
                                ewaste_yes_btn_status = 'Fail'
                                log_test_result("Verify that ewaste_yes_btn should be tapped successful",
                                                ewaste_yes_btn_status)

                        else:
                            ewaste_not_sure_back_arrow_status = 'Fail'
                            log_test_result("Verify that ewaste_not_sure_back_arrow should be tapped successful",
                                            ewaste_not_sure_back_arrow_status)

                    else:
                        ewaste_not_sure_btn_status = 'Fail'
                        log_test_result("Verify that ewaste_not_sure_btn should be tapped successful",
                                        ewaste_not_sure_btn_status)

                else:
                    ewaste_action_btn_not_sure_status = 'Fail'
                    log_test_result("Verify that Ewaste action button should be tapped again",
                                    ewaste_action_btn_not_sure_status)
            else:
                ewaste_no_arrow_status = 'Fail'
                log_test_result("Verify that Ewaste NO flow arrow  should be tapped successfully",
                                ewaste_no_arrow_status)
        else:
            ewaste_no_btn_status = 'Fail'
            log_test_result("Verify that Ewaste NO button should be tapped successfully", ewaste_no_btn_status)

    else:
        ewaste_action_btn_status = 'Fail'
        log_test_result("Verify that Ewaste action button should be tapped successfully",
                        ewaste_action_btn_status)


def log_test_result(test_name, status):
    csv_file = "Results/Ewaste_results.csv"
    csv_headers = ["Tests Summary", "Status"]
    csv_rows = [{"Tests Summary": test_name, "Status": status}]  # Wrapping rows in a list of dictionaries

    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_headers)

        # Check if the file is empty to write the header
        if file.tell() == 0:
            writer.writeheader()

        writer.writerows(csv_rows)


if __name__ == "__main__":
    pytest.main()
    # pytest.test_Ewaste()
