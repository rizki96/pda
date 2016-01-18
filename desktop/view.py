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

    NAME = 'WebFormMediator'
    pageHub = None

    def __init__(self, viewComponent):
        super(MainFormMediator, self).__init__(MainFormMediator.NAME, viewComponent)

        # default form
        self.load_form({'name': 'main', 'title': 'Aside-Test'})

    def listNotificationInterests(self):
        return [
            main.MainAppFacade.SHOW_FORM,
        ]

    def handleNotification(self, note):
        note_name = note.getName()

        if note_name == main.MainAppFacade.SHOW_FORM:
            params = dict(note.getBody())
            self.load_form(params)

    def handleHooks(self, **kwargs):
        if 'action' in kwargs:
            pass

    def load_form(self, params):
        current_path = utils.root_dir()
        #logging.info(current_path)
        aside_js = None
        variables = params["vars"] if "vars" in params else {}
        content = pages.retrieve(params["name"], BASE_PATH=current_path, ASIDE_JS=aside_js, TITLE=params["title"],
                                 **variables)
        self.viewComponent.webView.setHtml(*content)
