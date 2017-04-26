Including YAML files within YAML files
======================================

:date: 2017-04-26 12:05
:modified: 2017-04-26 12:05
:tags: YAML
:category: Computing
:slug: yaml-includes
:authors: David Hall
:summary: A custom PyYAML Loader class for reading nested YAML config files

*This blog entry has been copied from* `my particle physics blog <https://higgshunter.wordpress.com/2013/06/08/yaml-file-includes/>`_

I have written an extension to the PyYAML Loader class that allows you to include/import YAML files from within another YAML file.

I’m currently writing a program that will data from a YAML file and create a CV using a template engine. To aid flexibility, I wanted to allow the user to be able to include separate YAML files (e.g. education.yaml, skills.yaml, etc) within a master YAML file which would then be used to make the CV.

An initial search found `this <http://stackoverflow.com/questions/528281/how-can-i-include-an-yaml-file-inside-another>`_, which allows users to include a YAML file from within another. However, it’s quite a limited solution – it assumes you only want to include a single file. For my CV program, I wanted to be able to include multiple files within a single section. This could let you have separate files containing publications according to subject, and then include different groups of publications for different CVs.

My solution now supports all three kinds of YAML node: scalar, sequence and mapping. The class could alternatively derive from ``yaml.CLoader`` for improved performance when the C++ LibYAML bindings are available.

.. code-block:: python

    import yaml
    import os.path

    class Loader(yaml.Loader):
        def __init__(self, stream):
            self._root = os.path.split(stream.name)[0]
            super(Loader, self).__init__(stream)
            Loader.add_constructor('!include', Loader.include)
            Loader.add_constructor('!import',  Loader.include)

        def include(self, node):
            if isinstance(node, yaml.ScalarNode):
                return self.extractFile(self.construct_scalar(node))

            elif isinstance(node, yaml.SequenceNode):
                result = []
                for filename in self.construct_sequence(node):
                    result += self.extractFile(filename)
                return result

            elif isinstance(node, yaml.MappingNode):
                result = {}
                for k,v in self.construct_mapping(node).iteritems():
                    result[k] = self.extractFile(v)
                return result

            else:
                print "Error:: unrecognised node type in !include statement"
                raise yaml.constructor.ConstructorError

        def extractFile(self, filename):
            filepath = os.path.join(self._root, filename)
            with open(filepath, 'r') as f:
                return yaml.load(f, Loader)

Please note that the arguments to ``!include`` and ``!import`` must be on the same line (due to PyYAML parser).
This allows you to specify YAML files like:

.. code-block:: yaml

    education:    !include education.yaml

    activities:   !include [schools.yaml, conferences.yaml, workshops.yaml]

    publications: !include {peer_reviewed: publications/peer_reviewed.yaml, internal: publications/internal.yaml}

This Loader class is passed to ``yaml.load()`` like so:

.. code-block:: python

    from yaml import load

    with open('document.yaml', 'r') as f:
        data = load(f, Loader=Loader)
