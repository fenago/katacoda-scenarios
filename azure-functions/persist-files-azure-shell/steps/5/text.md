Cloud Shell persists files through both of the following methods:

- Creating a disk image of your `$Home` directory to persist all contents within the directory. The disk image is saved in your specified file share as `acc_<User>.img` at fileshare.storage.windows.net/fileshare/.cloudconsole/acc_<User>.img, and it automatically syncs changes.

- Mounting your specified file share as `clouddrive` in your `$Home` directory for direct file-share interaction. /Home/<User>/clouddrive is mapped to **fileshare.storage.windows.net/fileshare**.

**Note:** All files in your `$Home` directory, such as SSH keys, are persisted in your user disk image, which is stored in your mounted file share. Apply best practices when you persist information in your $Home directory and mounted file share.