'''
PIN file generator
'''


import argparse
import os
from gooey import Gooey, GooeyParser

pinTemplate = """\
{{
   "URL": "ssh://git@code.citrite.net/{repo}/{pinRepo}.git",
   "commitish": "{branch}",
   "patchqueue": "{branch}"
}}
"""


@Gooey()
def main():
    parser = GooeyParser()

    parser.add_argument(
        'repo',
        default='~weix',
        action='store')

    parser.add_argument(
        'branch',
        default='private/weix/req-440',
        action='store')

    parser.add_argument(
        'pinRepo',
        default='guest-templates-json;linux-guest-loader;xenserver-pv-tools',
        action='store')

    parser.add_argument(
        'path',
        default=r'g:/tmp/1',
        action='store')

    args = parser.parse_args()
    
    for i in args.pinRepo.split(';'):
        content = pinTemplate.format(repo=args.repo, pinRepo=i,
                                 branch=args.branch)
        f = open(os.path.join(args.path,i+'.pin'),'wb')                         
        f.write(content)
        f.close()
        print i + ': OK.'                         


if __name__ == '__main__':
    main()
