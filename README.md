# Artemis Pfs Unpacker
Python port of C# unpacker - https://github.com/Azukee/Macaron

I don't have or wanted to install VS/Mono xbuild didn't work.

You could easily(I imagine) write a repacker by doing the steps in reverse. Though you'd have to repack all the files as the XOR'd files are done off a hash of the header table. AKA if you change a single offset or size it'd make a new SHAKey not allowing the game to unXOR the files correctly.
