def test_test_file(host):
    f = host.file("/etc/test.txt")
    assert f.exists
    assert f.is_file
    assert f.content_string == "TEST\n"


def test_nginx_package(host):
    s = host.package("nginx")
    assert s.is_installed


def test_nginx_service(host):
    s = host.service("nginx")
    assert s.is_enabled
    assert s.is_running
