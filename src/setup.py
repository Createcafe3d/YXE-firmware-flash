from setuptools import setup
from setuptools.command.install import install as _Install
from VERSION import version

setup(
    name='YXE3DFirmwareAPI',
    version=version,
    description='Tool for updating the firmware of YXE3D',
    options={},
    url="http://www.YXE3D.com",
    author="Peachy Printer",
    author_email="software+YXE3Dtools@YXE3D.com",
    install_requires=[],
    packages=['firmware', ],
    py_modules=['VERSION'],
    include_package_data=True
      )


class install(_Install):
    def run(self):
        super(install, self).run(self)
        print "BADA-BADA-KABONG"
