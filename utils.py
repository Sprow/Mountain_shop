import os
import uuid

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.__class__.__name__.lower(), filename)

def gen_page_list(page_number, page_count):
    """
    Pagination generator
    """
    my_page = []
    if page_count > 10:
        if page_number <= 4:
            for key in range(1, 7):
                my_page.append(key)
            my_page.append(u"...")
        elif page_number >= (page_count-4):
            for key in range((page_count-5), page_count+1):
                my_page.append(key)
        else:
            for key in range((page_number-2), (page_number+2)):
                my_page.append(key)
    else:
        for key in range(0, page_count):
            my_page.append(key+1)
    return my_page