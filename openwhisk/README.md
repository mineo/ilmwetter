# Openwhisk support

The files in this directory allow deploying the scraper
to [Apache OpenWhisk](http://openwhisk.incubator.apache.org/). The Makefile's
default target (`all`) creates a zip file containing the installed scraper and
its dependencies, the `create-action` target uses
the
[OpenWhisk CLI](https://github.com/apache/incubator-openwhisk/blob/master/docs/README.md#setting-up-the-openwhisk-cli) to
upload it as an action to an OpenWhisk instance.
