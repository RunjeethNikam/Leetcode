from abc import ABC


class CloudStorage(ABC):
    """
    `CloudStorage` interface.
    """

    def add_file(self, name: str, size: int) -> bool:
        """
        Should add a new file `name` to the storage.
        `size` is the amount of memory required in bytes.
        The current operation fails if a file with the same `name`
        already exists.
        Returns `True` if the file was added successfully or `False`
        otherwise.
        """
        # default implementation
        return False

    def copy_file(self, name_from: str, name_to: str) -> bool:
        """
        Should copy the file at `name_from` to `name_to`.
        The operation fails if `name_from` points to a file that
        does not exist or points to a directory.
        The operation fails if the specified file already exists at
        `name_to`.
        Returns `True` if the file was copied successfully or
        `False` otherwise.
        """
        # default implementation
        return False

    def get_file_size(self, name: str) -> int | None:
        """
        Should return the size of the file `name` if it exists, or
        `None` otherwise.
        """
        # default implementation
        return None
    
    def find_file(self, prefix: str, suffix: str) -> list[str]:
        """
        Should search for files with names starting with `prefix`
        and ending with `suffix`.
        Returns a list of strings representing all matching files in
        this format:
        `["<name_1>(<size_1>)", "<name_2>(<size_2>)", ...]`.
        The output should be sorted in descending order of file
        sizes or, in the case of ties,
        [lexicographically](keyword://lexicographical-order-for-
        strings).
        If no files match the required properties, should return an
        empty list.
        """
        # default implementation
        return []
    def add_user(self, user_id: str, capacity: int) -> bool:
        """
        Should add a new user to the system, with `capacity` as
        their storage limit in bytes.
        The total size of all files owned by `user_id` cannot exceed
        `capacity`.
        The operation fails if a user with `user_id` already exists.
        Returns `True` if a user with `user_id` is successfully
        created, or `False` otherwise.
        """
        # default implementation
        return False

    def add_file_by(self, user_id: str, name: str, size: int) -> int | None:
        """
        Should behave in the same way as the `add_file` from Level
        1, but the added file should be owned by the user with
        `user_id`.
        A new file cannot be added to the storage if doing so will
        exceed the user's `capacity` limit.
        Returns the remaining storage capacity for `user_id` if the
        file is successfully added or `None` otherwise.
        
        *Note that* all queries calling the `add_file` operation
        implemented during Level 1 are run by the user with
        `user_id = "admin"`, who has unlimited storage capacity.
        Also, assume that the `copy_file` operation preserves the
        ownership of the original file.
        """
        # default implementation
        return None

from collections import defaultdict


class CloudStorageImpl(CloudStorage):

    def __init__(self):
        # TODO: implement
        self.fs = defaultdict(dict)
        self.users = dict()

    def add_file(self, name: str, size: int) -> bool:
        if name in self.fs:
            return False
        self.fs[name]["size"] = size
        return True
    
    def copy_file(self, name_from: str, name_to: str) -> bool:
        if name_to in self.fs or name_from not in self.fs:
            return False
        user_id = self.fs[name_from].get('owner', 'admin')
        if user_id == "admin":
            self.fs[name_to] = self.fs[name_from].copy()
            return True
        else:
            used = self.users[user_id]['used']
            size = self.fs[name_from]['size']
            cap = self.users[user_id]['cap']
            if used + size <= cap:
                self.fs[name_to] = self.fs[name_from].copy()
                self.users[user_id]['used'] += size
                return True
            else:
                return False
    
    def get_file_size(self, name: str) -> int | None:
        if name not in self.fs:
            return None
        
        return self.fs[name]["size"]
    
    def find_file(self, prefix: str, suffix: str) -> list[str]:
        result = []
        key: str
        for key, value in self.fs.items():
            if key.startswith(prefix) and key.endswith(suffix):
                result.append((key, value["size"]))
        result.sort(key=lambda item: (-item[1], item[0]))
        return list(map(lambda item: f"{item[0]}({item[1]})", result))
    
    def add_user(self, user_id: str, capacity: int) -> bool:
        if user_id in self.users:
            return False
        
        self.users[user_id] = {"cap": capacity, "used": 0}
        return True

    def add_file_by(self, user_id: str, name: str, size: int) -> int | None:
        if name in self.fs or user_id not in self.users:
            return None
        if self.users[user_id]['used'] + size > self.users[user_id]['cap']:
            return None
        self.fs[name]["size"] = size
        self.fs[name]['owner'] = user_id
        self.users[user_id]['used'] += size
        return self.users[user_id]['cap'] - self.users[user_id]['used']
    
    def update_capacity(self, user_id: str, capacity: int) -> int | None:
        if user_id not in self.users:
            return None
        if capacity >= self.users[user_id]['cap']:
            return 0
        result = []
        total_capacity = 0
        for key, value in self.fs.items():
            if value.get('owner', 'admin') == user_id:
                total_capacity += value['size']
                result.append((key, value["size"]))
        result.sort(key=lambda item: (-item[1], item[0]), reverse=True)
        count = 0
        while total_capacity > capacity:
            key, value = result.pop()
            total_capacity -= value
            del self.fs[key]
            count += 1
        self.users[user_id]["used"] = total_capacity
        self.users[user_id]['cap'] = capacity
        return count
    
    def compress_file(self, user_id: str, name: str) -> int | None:
        if name not in self.fs or user_id not in self.users or (name + '.COMPRESSED') in self.fs:
            return None
        value = self.fs[name].copy()
        if user_id == value['owner']:
            del self.fs[name]
            name = name + '.COMPRESSED'
            self.fs[name] = value
            size = value['size']
            value['size'] -= size//2
            self.users[user_id]['used'] -= size//2
            return self.users[user_id]['cap'] - self.users[user_id]['used']
        else:
            return None

    def decompress_file(self, user_id: str, name: str) -> int | None:
        if name not in self.fs or name.removesuffix('.COMPRESSED') in self.fs or user_id not in self.users:
            return None
        value = self.fs[name].copy()
        if user_id == value['owner'] and value['size'] + self.users[user_id]['used'] <= self.users[user_id]['cap']:
            del self.fs[name]
            name = name.removesuffix('.COMPRESSED')
            size = value['size']
            self.fs[name] = value
            self.users[user_id]['used'] += size
            value['size'] = 2 * size
            return self.users[user_id]['cap'] - self.users[user_id]['used']

        else:
            return None
        
        


    


storage = CloudStorageImpl()
 

# def test_level_1_case_01_add_and_get_file_in_directory(self):
#     self.assertTrue(self.storage.add_file('/dir/file.txt', 10))
#     self.assertEqual(self.storage.get_file_size('/dir/file.txt'), 10)

# # @timeout(0.4)
# def test_level_1_case_02_add_and_get_files(self):
#     self.assertTrue(self.storage.add_file('/directory/dir/file1.txt', 15))
#     self.assertTrue(self.storage.add_file('/file2', 79))
#     self.assertEqual(self.storage.get_file_size('/directory/dir/file1.txt'), 15)
#     self.assertEqual(self.storage.get_file_size('/directory/dir/file1.txt'), 15)
#     self.assertEqual(self.storage.get_file_size('/file2'), 79)

# @timeout(0.4)
def test_level_1_case_03_add_copy_and_get_files():
    storage.add_file('/dir/file1.mov', 20)
    storage.copy_file('/dir/file1.mov', '/file2.mp4')
    storage.get_file_size('/dir/file1.mov')
    storage.get_file_size('/file2.mp4')
test_level_1_case_03_add_copy_and_get_files()