from setuptools import setup
import setup_translate

pkg = 'Extensions.DreamExplorer'
setup(name='enigma2-plugin-extensions-dreamexplorer',
       version='3.0',
       description='DreamExplorer: Manage files on your Dreambox',
       package_dir={pkg: 'DreamExplorer'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'LICENSE', 'pyc2xml', 'dreamexplorer.png', 'res/*.png', 'res/*.mvi']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
