__author__ = 'rizki'

import os
import sys

import puremvc.interfaces
import puremvc.patterns.mediator

import main
#import vo
#import model
import utils

from aside import pages, events, components


class MainFormMediator(puremvc.patterns.mediator.Mediator, puremvc.interfaces.IMediator):

    NAME = 'MainFormMediator'

    def __init__(self, viewComponent):
        super(MainFormMediator, self).__init__(MainFormMediator.NAME, viewComponent)

        # default form
        self.load_form({'name': 'main', 'title': 'Aside-Test'})

    def listNotificationInterests(self):
        return [
            main.MainAppFacade.DISPLAY_PAGE,
        ]

    def handleNotification(self, note):
        note_name = note.getName()

        if note_name == main.MainAppFacade.DISPLAY_PAGE:
            params = dict(note.getBody())
            self.load_form(params)

    def handleHooks(self, **kwargs):
        if 'action' in kwargs:
            pass

    def load_form(self, params):
        current_path = utils.root_dir()
        variables = params["vars"] if "vars" in params else {}
        content = pages.retrieve(params["name"], BASE_PATH=current_path, ASIDE_JS=None, TITLE=params["title"],
                                 **variables)
        self.viewComponent.webView.setHtml(*content)
