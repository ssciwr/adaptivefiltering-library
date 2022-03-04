import adaptivefiltering
import os

# Check that the filter library can be added
adaptivefiltering.add_filter_library(os.path.join(os.getcwd(), "adaptivefiltering_library"))

# Iterate over libraries and check metadata
for lib in adaptivefiltering.library.get_filter_libraries():
    for f in lib.filters:
        assert f.title != ""
        assert f.author != ""
        assert len(f.keywords) > 0
