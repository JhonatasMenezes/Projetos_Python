from torre_de_hanoi import torre_de_hanoi
import PySimpleGUI as sg
from PySimpleGUI import PySimpleGUI as sg

sg.popup("Hey Babe",
    title = 'First Window',
    button_color = 'blue',
    background_color = 'grey',
    text_color = 'white',
    button_type = 0,
    auto_close = False,
    auto_close_duration = None,
    custom_text = (None, None),
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    any_key_closes = False,
    image = None,
    modal = True)
sg.popup_ok('popup_ok')  # Shows OK button
sg.popup_yes_no('popup_yes_no')  # Shows Yes and No buttons
sg.popup_cancel('popup_cancel')  # Shows Cancelled button
sg.popup_ok_cancel('popup_ok_cancel')  # Shows OK and Cancel buttons
sg.popup_error('popup_error')  # Shows red error button
sg.popup_timed('popup_timed')  # Automatically closes
sg.popup_auto_close('popup_auto_close')  # Same as PopupTimed

