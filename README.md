Python Module Security Admonition
=================================

If you are reading this admonition while running pip, I'd like to take
this time to inform you that you just ran arbitrary code from the untrusted
internet (maybe even as root?). The fact that this was so easy is a bit of a
problem.

Remember when RubyGems.org got compromised and was down since they weren't
sure whether there were any problems with the gems themselves? That could
have just as easily been PyPI. Adding SSL to PyPI and certificate checking
to pip were big steps forward, but we need to make shipping and installing
modules securely even easier. I'm not sure whether that means developer
certificates or package signing or something else, but we need to find a
way to run only trusted code. As long as a one character typo can root your
box, the problem persists.

https://github.com/davidfischer/requestes
