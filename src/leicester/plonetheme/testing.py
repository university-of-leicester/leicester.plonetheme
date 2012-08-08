from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class LeicesterPlonetheme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import leicester.plonetheme
        xmlconfig.file('configure.zcml',
                       leicester.plonetheme,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'leicester.plonetheme:default')

LEICESTER_PLONETHEME_FIXTURE = LeicesterPlonetheme()
LEICESTER_PLONETHEME_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(LEICESTER_PLONETHEME_FIXTURE, ),
                       name="LeicesterPlonetheme:Integration")