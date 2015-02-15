import clang.cindex
import inspect

def dump(indent, node):
    # print node
    # print "kind.name", node.kind.name
    # if node.kind.name == "BINARY_OPERATOR":
    #     print "kind.name", node.kind.name
    #     # print node.location
    #     # print node.location.offset
    #     # print node.canonical
    #     tokens = []
    #
    #     x = 0
    #     for c in node.get_children():
    #         tokens = []
    #         for t in c.get_tokens():
    #             tokens.append(t.spelling)
    #
    #         print x, tokens 
    #         x += 1
    #
    #
    #     return
    print "%s%s: %s: %s" % (" "*indent, node.kind.name, node.displayname, node.spelling)
    x = 0
    for c in node.get_children():
        tokens = []
        for t in c.get_tokens():
            tokens.append(t.spelling)

        print " " * indent, x, tokens
        x += 1
    # print "displayname", node.displayname
    # print "spelling", node.spelling
    # print "usr", node.get_usr()
    # print "extent", node.extent
    # print "xdata", node.xdata
    # print "data", node.data

    for c in node.get_children():
        dump(indent+1, c)

index = clang.cindex.Index.create()
tu = index.parse("sample.cpp", ['-x', 'c++', '-std=c++11'])
print 'Translation unit:', tu.spelling
dump(0, tu.cursor)
