# This script takes a tab-separated input file with C. elegans
# gene names in the first column and Wormbase unique gene identifiers
# in the second, and produces a gene report file in html format with
# hyperlinks to Wormbase.

# open input and output files
gene_data = open('daf-16_only_down_simplemine.txt')
gene_report = open('daf-16_only_down.html', 'w')

# write outer html opening tags
print('<html>', file=gene_report)
print('<body>', file=gene_report)

# read lines of input (one line = one gene) and write one html
# paragraph per gene to the output
for line in gene_data:
    # each line has its fields separated by tabs
    fields = line.split('\t')
    if fields[1][:6] == 'WBGene':
        # The second column consists of something that looks
        # like a Wormbase gene identifier that we can link to.
        print(
            # start a new paragraph and a contained anchor with a
            # hyperlink
            '<p><a href="https://wormbase.org/species/c_elegans/gene/'
            + fields[1]   # unique part of hyperlink
            + '">'        # finish <a href="
            + fields[0]   # gene name shown to the user
            + '</a></p>', # anchor and paragraph closing tags
            file=gene_report
            )
    else:
        # There is no Wormbase gene identifier in the second column
        # so instead of generating a hyperlink we just turn the first column
        # into a really simple html paragraph.
        print('<p>' + fields[0] + '</p>', file=gene_report)

# write outer html closing tags
print('</body>', file=gene_report)
print('</html>', file=gene_report)

# close input and output files
gene_data.close()
gene_report.close()
