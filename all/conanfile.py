import shutil
import os
from conans.tools import download, unzip, check_md5, check_sha1, check_sha256
from conans import ConanFile, CMake, tools


class DurakComputerControlledOpponent(ConanFile):
    name = "durak_computer_controlled_opponent"
    homepage = "https://github.com/werto87/durak_computer_controlled_opponent"
    description = "Create a lookup table for durak"
    topics = ("computer_controlled_opponent")
    license = "BSL-1.0"
    url = "https://github.com/conan-io/conan-center-index"
    settings = "compiler"
    no_copy_source = True
    generators = "cmake"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def configure(self):
        self.options["soci"].with_boost = True
        self.options["soci"].with_sqlite3 = True

    def requirements(self):
        self.requires("durak/0.0.9@werto87/stable")
        self.requires("st_tree/1.2.1")
        self.requires("boost/1.78.0")
        self.requires("small_memory_tree/0.0.1")
        self.requires("range-v3/0.12.0")
        self.requires("confu_soci/0.3.2@werto87/stable")
        

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build(args=["--target durak_computer_controlled_opponent"])

    def package(self):
        self.copy("*.h*",
                  dst="include/durak_computer_controlled_opponent",
                  src="source_subfolder/durak_computer_controlled_opponent")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["durak_computer_controlled_opponent"]