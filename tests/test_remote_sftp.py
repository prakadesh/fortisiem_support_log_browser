import os
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import Mock

from ssh_client import RemoteSFTPClient, SFTPDownloadCancelled


class RemoteSFTPClientTests(unittest.TestCase):
    def test_list_tar_files_is_newest_first_and_limited(self):
        client = RemoteSFTPClient("host", "user")
        client.connect = Mock()
        client.close = Mock()
        client.sftp = Mock()
        client.sftp.listdir_attr.return_value = [
            SimpleNamespace(filename=f"archive-{i}.tar", st_size=i, st_mtime=i)
            for i in range(12)
        ] + [SimpleNamespace(filename="not-an-archive.txt", st_size=1, st_mtime=99)]

        files = client.list_tar_files()

        self.assertEqual(10, len(files))
        self.assertEqual("archive-11.tar", files[0]["name"])
        self.assertEqual("archive-2.tar", files[-1]["name"])
        client.close.assert_called_once()

    def test_cancelled_download_removes_partial_file_and_closes_sessions(self):
        client = RemoteSFTPClient("host", "user")
        client.connect = Mock()
        client.close = Mock()
        client.sftp = Mock()
        client.sftp.stat.return_value = SimpleNamespace(st_size=4)
        with tempfile.TemporaryDirectory() as directory:
            destination = os.path.join(directory, "partial.tar")

            def partial_get(path, local_path, callback):
                with open(local_path, "wb") as file_handle:
                    file_handle.write(b"data")
                callback(4, 4)

            client.sftp.get.side_effect = partial_get
            cancel = Mock(is_set=Mock(return_value=True))
            with self.assertRaises(SFTPDownloadCancelled):
                client.download_remote_file_sftp({"path": "/tmp/a.tar", "size": 4}, destination, cancel_event=cancel)
            self.assertFalse(os.path.exists(destination))
        client.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
