import afwizard
import os

# Check that the filter library can be added
afwizard.add_filter_library(os.path.join(os.getcwd(), "afwizard_library"))

# Iterate over libraries and check metadata
for lib in afwizard.library.get_filter_libraries():
    for f in lib.filters:
        assert f.title != ""
        assert f.author != ""
        assert len(f.keywords) > 0
